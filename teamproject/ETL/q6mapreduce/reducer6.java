package q6redu;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
//output the direct answer locally
public class reducer6 {
	public static void main(String args[]) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in,"UTF8"));
		File fileDir = new File("/Users/JiateLi/Desktop/finalq6.txt");
        OutputStreamWriter output = new OutputStreamWriter(new FileOutputStream(fileDir),"UTF-8");
		String input;
		int count = 0;
		int sum = 0;
		int lastsum = 0;
		String uid = null;
		while ((input=br.readLine())!=null){
			String[] parts = input.split("\t");
			uid = parts[0];
			count = Integer.parseInt(parts[1]);
			sum = sum + count;
			output.write(uid + "\t"+ sum + "\t"+ lastsum + "\n");
			lastsum = sum;
			output.flush();
		}
		output.close();
	}
}
