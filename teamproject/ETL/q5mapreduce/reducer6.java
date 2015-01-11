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
//used in local, input is nooverlop.txt, I will modify chongfu to new
public class reducer6 {
	public static void main (String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in,"UTF8"));
		File fileDir = new File("/Users/JiateLi/Desktop/newnooverlop.txt");
        OutputStreamWriter output = new OutputStreamWriter(new FileOutputStream(fileDir),"UTF-8");
		String input = null;
		String uid = null;
		String oriuid = null;
		String lastuid = null;
		String lastoriuid = null;
		while((input=br.readLine())!=null){
			String[] part=input.split("\t");
			uid = part[0];
			oriuid = part[1];
			if(!oriuid.equals("none")){
				if(uid.equals(lastuid)){
					if(!oriuid.equals(lastoriuid)){
						output.write(uid + "\t" + oriuid + "\t" + "0" + "\n");
						output.flush();
						lastoriuid = oriuid;
					}
					else{
						output.write(uid + "\t" + oriuid + "\t" + "1" + "\n");//chongfu 
						output.flush();
					}
				}
				else{
					output.write(uid + "\t" + oriuid + "\t" + "0" + "\n");
					output.flush();
					lastuid = uid;
					lastoriuid = oriuid;
				}
			}
			else{
				output.write(uid + "\t" + oriuid + "\t" + "0" + "\n");
				output.flush();
				lastuid = uid;
				lastoriuid = oriuid;
			}
		}
	    output.close();
	}
}
