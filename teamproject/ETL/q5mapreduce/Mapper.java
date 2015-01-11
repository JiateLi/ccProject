package q5map;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

public class Mapper {
	public static void main(String args[]) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final JSONParser parser = new JSONParser();
		String line = null;
		while ((line = br.readLine()) != null) {
			line = line.trim();
			if(line.isEmpty()) {
				continue;
			}
			String ori_uid = "none";
			JSONObject tweetcont = (JSONObject)parser.parse(line);
			JSONObject user = (JSONObject)tweetcont.get("user");
			String user_id = user.get("id").toString();
			String tweet_id = tweetcont.get("id").toString();
			
			JSONObject retweeted_status = (JSONObject)tweetcont.get("retweeted_status");
			if(retweeted_status!=null){
				JSONObject ori_user = (JSONObject)retweeted_status.get("user");
				if(ori_user!=null){
					ori_uid = ori_user.get("id").toString();
				}
				else{
					ori_uid = "none";
				}
			}
			PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out, "UTF-8"),true);
			out.println(user_id + "\t" + tweet_id+ "\t" + ori_uid);
		}		
		br.close();
	}
}
