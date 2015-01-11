package q6redu;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
//output the no overlop locally
public class reducer4 {
	public static void main(String args[]) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in,"UTF8"));
		File fileDir = new File("/Users/JiateLi/Desktop/nooverq6.txt");
        OutputStreamWriter output = new OutputStreamWriter(new FileOutputStream(fileDir),"UTF-8");
		String input;
		int count = 0;
		String tid = null;
		String uid = null;
		String curtid = null;
		while ((input=br.readLine())!=null){
			String[] parts = input.split("\t");
			tid = parts[1];
			uid = parts[0];
			count = Integer.parseInt(parts[2]);
			if(tid!=null){
				if(!tid.equals(curtid)){
					output.write(uid + "\t" + count + "\n");
					output.flush();
					curtid = tid;
				}
				else{	
				}
			}
		}		
		output.close();
	}
}
