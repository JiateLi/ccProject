package q6redu;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
//output the direct answer locally
public class reducer5 {
	public static void main(String args[]) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in,"UTF8"));
		File fileDir = new File("/Users/JiateLi/Desktop/allq6.txt");
        OutputStreamWriter output = new OutputStreamWriter(new FileOutputStream(fileDir),"UTF-8");
		String input;
		int currentCount = 0;
		int count = 0;
		String uid = null;
		String curuid = null;
		while ((input=br.readLine())!=null){
			String[] parts = input.split("\t");
			uid = parts[0];
			count = Integer.parseInt(parts[1]);
			if(curuid!=null && uid.equals(curuid)){//uid is still the same
				currentCount = currentCount + count;
			}
			else{
				if(curuid!=null){
					output.write(curuid + "\t"+ currentCount + "\n");
			    	output.flush();
				}
				currentCount = count;
				curuid = uid;
			}
		}
		//print out last word if missed 
		if (curuid!=null && uid.equals(curuid)){
			output.write(curuid + "\t"+ currentCount + "\n");
	    	output.flush();
		}
		output.close();
	}
}
