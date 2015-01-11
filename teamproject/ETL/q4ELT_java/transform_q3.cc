#include <iostream>
#include <stdint.h>
#include <set>
#include <string>
#include <vector>
#include <map>

using std::string;
using std::vector;
typedef std::pair<uint64_t, uint64_t> Retweeted;
typedef std::map<Retweeted, bool> mmap;
/*class PackIter {
 public:
  int n;
  FILE* fin;
  PackIter(const string &fname, const int pack_num) {
    fin = fopen(fname.c_str(), "r");
    n = pack_num;
  }
  ~PackIter() {
    fclose(fin);
  }
  bool next(std::vector<Retweeted> &vec) {
    uint64_t uid, orig;
    for (int i = 0; i < n; i++) {
      if (fscanf(fin, "%llu%llu", &uid, &orig) == EOF) {
        return false;
      } else {
        vec.push_back(Retweeted(uid, orig));
      }
    }
    return true;
  }
  bool next1(uint64_t &retweet, uint64_t &orig) {
    if (fscanf(fin, "%llu%llu", &retweet, &orig) == EOF) {
      return false;
    } else {
      return true;
    }
  }
  void resetFile() {
    fseek(fin, 0, SEEK_SET);
  }
};*/

int main(int argc, const char *argv[])
{
  mmap cache;
  FILE* fin = fopen("../part-00000", "r");
  uint64_t retweet, orig;
  while (fscanf(fin, "%llu%llu", &retweet, &orig) != EOF) {
    if (retweet == orig) {
      // if equal, then also has the reverse relationship
      cache.insert(std::pair<Retweeted, bool>(Retweeted(orig, retweet), true));
    } else {
      mmap::iterator it = cache.find(Retweeted(orig, retweet));
      // not exist in cache
      if (it == cache.end()) {
        it = cache.find(Retweeted(retweet, orig));
        if (it == cache.end()) {
          // can't find reverse relationship: `retweet` retweet `orig`
          cache.insert(std::pair<Retweeted, bool>(Retweeted(orig, retweet), false));
        } else {
          // find reverse relationship
          it->second = true;
          cache.insert(std::pair<Retweeted, bool>(Retweeted(orig, retweet), true));
        }
      }
    }
  }
  fclose(fin)
  FILE *fout = fopen("q3.out", "w");
  for (mmap::const_iterator it = cache.begin();
       it != cache.end(); it++) {
    if (it->second) {
      // A retweeted by B
      //printf("%llu\t%llu\t(%llu)\n", (it->first).first, (it->first).second, (it->first).second);
      fprintf(fout, "%llu\t%llu\t(%llu)\n", (it->first).first, (it->first).second, (it->first).second);
    } else {
      fprintf(fout, "%llu\t%llu\t%llu\n", (it->first).first, (it->first).second, (it->first).second);
      //printf("%llu\t%llu\t%llu\n", (it->first).first, (it->first).second, (it->first).second);
    }
  }
  fclose(fout);
  return 0;
}
