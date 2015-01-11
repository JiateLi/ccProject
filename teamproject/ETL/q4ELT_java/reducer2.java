import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.OutputStreamWriter;

public class reducer2 {
	public static void main(String args[]) throws Exception{
		BufferedReader br = 
				new BufferedReader(new InputStreamReader(System.in,"UTF8"));
		File fileDir = new File("/Users/JiateLi/Desktop/testwrite.txt");
        OutputStreamWriter output = new OutputStreamWriter(new FileOutputStream(fileDir),"UTF-8");
		
		String input;
		String time = null;
		String currentTime = null;
		String hashtag = null;
		String currentHashtag = null;
		String location = null;
		String currentLocation = null;
		String tidset = null;
		String outputstr = null;
		String curtidset = null;
		int rank = 0;
		
		while ((input=br.readLine())!=null){
			String[] parts = input.split("\t");
			time = parts[0];
			hashtag = parts[3];
			location = parts[1];
			tidset = parts[6];
			
			
			if(currentTime!=null && currentTime.equals(time)){//time is still the same  ??&& currentLocation!=null && currentHashtag!=null
				//currentCount++;
				if(currentLocation.equals(location)){//location is same
					if (currentHashtag.equals(hashtag)){
						
					}
					else{//now we change to same day same location but diff hastag
						rank++;
						outputstr = currentTime+"\t"+currentLocation +"\t"+ currentHashtag+"\t"+rank+"\t"+curtidset+"\n";
						output.write(outputstr);
						output.flush();
						currentHashtag = hashtag;
						curtidset=tidset;
					}
				}
					//System.out.println(currentTime+"\t"+currentLocation +"\t"+ hashtag+"\t"+rank+"\t"+tidset+"\n"); 
				else{//now we change to same day but diff location
					rank++;
					outputstr = currentTime+"\t"+currentLocation +"\t"+ currentHashtag+"\t"+rank+"\t"+curtidset+"\n";
					output.write(outputstr);
					output.flush();
					//System.out.println(currentTime+"\t"+currentLocation +"\t"+ hashtag+"\t"+rank+"\t"+tidset); 	
					currentLocation = location;
					curtidset=tidset;
					currentHashtag = hashtag;
					rank=0;
					}
				}
			else{//now we change to diff day or fist line
				if(currentTime!=null){//Is this the first time, if not output count
					rank++;
					outputstr = currentTime+"\t"+currentLocation +"\t"+ currentHashtag+"\t"+rank+"\t"+curtidset+"\n";
					output.write(outputstr);
					output.flush();
					//System.out.println(currentTime+"\t"+currentLocation +"\t"+ hashtag+"\t"+rank+"\t"+tidset); 	
				}
				currentLocation = location;
				currentTime = time;
				curtidset=tidset;
				currentHashtag = hashtag;
				rank=0;			
			}
		}
		//print out last word if missed 
		if (currentTime!=null && currentTime.equals(time)){
			rank++;
			outputstr = currentTime+"\t"+currentLocation +"\t"+ currentHashtag+"\t"+rank+"\t"+curtidset+"\n";
			output.write(outputstr);
			output.flush();
			//System.out.println(currentTime+"\t"+currentLocation +"\t"+ hashtag+"\t"+rank+"\t"+tidset); 	
		}
		output.close();
	}
}
