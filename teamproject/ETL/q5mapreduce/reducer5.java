package q5redu;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;
import java.io.File;
import java.io.FileOutputStream;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.OutputStreamWriter;

public class reducer5 {
	public static void main (String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in,"UTF8"));
		File fileDir = new File("/Users/JiateLi/Desktop/final5.txt");
        OutputStreamWriter output = new OutputStreamWriter(new FileOutputStream(fileDir),"UTF-8");

		String input = null;		
		String uid = null;
		String curuid = null;
		int curscore1 = 0;
		int curscore2 = 0;
		int curscore3 = 0;
		int curscore4 = 0;
		int score1 = 0;
		int score2 = 0;
		int score3 = 0;
		int score4 = 0;
		while((input=br.readLine())!=null){
			String[] part=input.split("\t");
			uid = part[0];
			score1 = Integer.parseInt(part[1]);
			score2 = Integer.parseInt(part[2]);
			score3 = Integer.parseInt(part[3]);
			score4 = Integer.parseInt(part[4]);
	
			if(curuid!=null && curuid.equals(uid)){
                curscore1 = score1 + curscore1;
				curscore2 = score2 + curscore2;
				curscore3 = score3 + curscore3;
				curscore4 = score4 + curscore4;
			}
			else{
				if(curuid!=null){
					output.write(curuid+"\t"+curscore1 +"\t"+ curscore2 + "\t" + curscore3 + "\t" + curscore4 + "\n");
					output.flush();	
				}
				curuid = uid;
				curscore1 = score1;
				curscore2 = score2;
				curscore3 = score3;
				curscore4 = score4;
			}
	    }
		if (curuid!=null && curuid.equals(uid)){
			output.write(curuid+"\t"+curscore1 +"\t"+ curscore2 + "\t" + curscore3 + "\t" + curscore4 + "\n");
			output.flush();	
		}
	    output.close();
	}
}
