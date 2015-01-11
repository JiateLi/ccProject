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
//get the nooverlop.txt
public class reducer2 {
	public static void main (String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in,"UTF8"));
		File fileDir = new File("/Users/JiateLi/Desktop/nooverlop.txt");
        OutputStreamWriter output = new OutputStreamWriter(new FileOutputStream(fileDir),"UTF-8");

		String input = null;
		
		String tid = null;
		String cur_tid = null;
		String cur_uid = null;
		String cur_oriuid = null;

		while((input=br.readLine())!=null){
			String[] part=input.split("\t");
			cur_uid = part[0];
			cur_tid = part[1];
			cur_oriuid = part[2];
			if(cur_tid!=null){
				if(!cur_tid.equals(tid)){
					output.write(cur_uid + "\t" + cur_oriuid + "\n");
					output.flush();
					tid = cur_tid;
				}
				else{	
				}
			}
		}
		output.close();
	}
}
