import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.File;
import java.io.FileInputStream;  

public class mapper {
	public static void main(String args[]){
		try{
			//File fileDir = new File("/Users/JiateLi/Desktop/q4test.txt");

			BufferedReader br = 
					new BufferedReader(new InputStreamReader(System.in, "UTF8"));
			//BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(fileDir), "UTF8"));
			String input;
			String time = null;
			String timeout = null;
			long tid = 0;
			String hashtag = null;
			int index = 0;
			String location = null;
			while ((input=br.readLine())!=null){
				String[] parts = input.split("\t");
				tid = Long.parseLong(parts[0]);
				time = parts[1];
				timeout = time.split(" ")[0];
				hashtag = parts[2];
				index = Integer.parseInt(parts[3]);
				location = parts[4];
				//int count = Integer.parseInt(parts[1]);
				System.out.println(timeout+"\t"+location +"\t"+ hashtag+"\t"+tid+"\t"+index);
			}
			//br.close();//use for file
		}catch(IOException io){
			io.printStackTrace();
		} 
	}
}
