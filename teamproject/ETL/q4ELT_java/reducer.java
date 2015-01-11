import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class reducer {
	public static void main(String args[]) throws Exception{
		BufferedReader br = 
				new BufferedReader(new InputStreamReader(System.in,"UTF8"));
		String input;
		int currentCount = 0;
		String time = null;
		String currentTime = null;
		//long tid = 0;
		String tid = null;
		String fir_tid = null;
		String hashtag = null;
		String currentHashtag = null;
		int index = 0;
		int fir_index = 0;
		String location = null;
		String currentLocation = null;
		StringBuffer tidset = new StringBuffer();
		String curtid = null;
		
		while ((input=br.readLine())!=null){
			String[] parts = input.split("\t");
			time = parts[0];
			tid = parts[3];
			hashtag = parts[2];
			index = Integer.parseInt(parts[4]);
			location = parts[1];
			
			if(currentTime!=null && currentTime.equals(time)){//time is still the same  ??&& currentLocation!=null && currentHashtag!=null
				//currentCount++;
				if(currentLocation.equals(location)){//location is same
					if(currentHashtag.equals(hashtag)){//in the same hashtag
						if(curtid.equals(tid)){
						}
						else{
							currentCount++;//hashtag count
							tidset.append(",");
							tidset.append(tid);//tid set
							curtid=tid;
						}
					}
					else{//now we change to same day same location but diff hashtag
						System.out.println(currentTime+"\t"+currentLocation +"\t"+ currentCount
								+"\t"+ currentHashtag+"\t"+fir_tid+"\t"+fir_index+"\t"+tidset.toString());
						currentHashtag = hashtag;
						fir_tid = tid;
						fir_index = index;
						tidset.setLength(0);//
						tidset.append(tid);
						curtid=tid;
						currentCount = 1;
					}
				}
				else{//now we change to same day but diff location
					System.out.println(currentTime+"\t"+currentLocation +"\t"+ currentCount
							+"\t"+ currentHashtag+"\t"+fir_tid+"\t"+fir_index+"\t"+tidset.toString());
					currentHashtag = hashtag;
					fir_tid = tid;
					fir_index = index;
					tidset.setLength(0);//
					tidset.append(tid);
					curtid=tid;
					currentCount = 1;
					currentLocation = location;
				}
			}
			else{//now we change to diff day or fist line
				if(currentTime!=null){//Is this the first time, if not output count
					System.out.println(currentTime+"\t"+currentLocation +"\t"+ currentCount
							+"\t"+ currentHashtag+"\t"+fir_tid+"\t"+fir_index+"\t"+tidset.toString());
				}
				currentHashtag = hashtag;
				fir_tid = tid;
				curtid=tid;
				fir_index = index;
				tidset.setLength(0);//
				tidset.append(tid);
				currentCount = 1;
				currentLocation = location;
				currentTime = time;
			}
		}
		//print out last word if missed 
		if (currentTime!=null && currentTime.equals(time)){
			System.out.println(currentTime+"\t"+currentLocation +"\t"+ currentCount
					+"\t"+ currentHashtag+"\t"+fir_tid+"\t"+fir_index+"\t"+tidset.toString());
		}
	}
}
