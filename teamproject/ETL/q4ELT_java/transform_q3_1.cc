#include <iostream>
#include <stdint.h>
#include <set>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cassert>

using namespace std;

typedef uint64_t ull;

template <class T>
int addToMMap(T &mmap, const ull orig, const ull retweet) {
  auto it = mmap.find(orig);
  if (it == mmap.end()) {
    auto ret = mmap.insert(pair<ull, set<ull> >(orig, set<ull>()));
    it = ret.first;
  }
  //if ((it->second).find(retweet) == (it->second).end()) {
  if (std::find(it->second.begin(), it->second.end(), retweet) == it->second.end()) {
    it->second.push_back(retweet);
  }
  return (it->second).size();
}

// a retweeted by b
template <class T>
bool isRetweetedBy(T &mmap, ull a, ull b) {
  typename T::const_iterator it = mmap.find(a);
  if (it == mmap.end()) return false;
  return (std::find(it->second.begin(), it->second.end(), retweet) != it->second.end());
  //return (it->second).find(b) != (it->second).end();
}

int main() {
  FILE* fin = fopen("q3-tmp", "r");
  ull retweet, orig;
  map<ull, vector<ull> > mmap;
  int max_len = 0;
  //set<pair<ull, ull> > mset;
  while (fscanf(fin, "%llu%llu", &retweet, &orig) != EOF) {
    int n = addToMMap(mmap, orig, retweet);
  }
  fclose(fin);
  cout << "load data finished" << endl;
  FILE* fout = fopen("q3.out", "w");
  for (auto map_it = mmap.begin(); map_it != mmap.end(); map_it++) {
    ull orig = map_it->first;
    fprintf(fout, "%llu\t", orig);
    for (auto set_it = map_it->second.begin();
         set_it != map_it->second.end();
         set_it++) {
      ull retweet = *set_it;
      if (isRetweetedBy(mmap, retweet, orig)) {
        fprintf(fout, "(%llu),", retweet);
      } else {
        fprintf(fout, "%llu,", retweet);
      }
    }
    fprintf(fout, "\n");
  }
  fclose(fout);
  return 0;
}
// 144438
