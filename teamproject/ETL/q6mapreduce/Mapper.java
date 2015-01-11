package cc;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Map;
import java.util.Set;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.util.HashMap;
import java.util.HashSet;


public class Mapper {
	public static void main(String args[]) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final JSONParser parser = new JSONParser();
		PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out, "UTF-8"),true);
		String line = null;
		while ((line = br.readLine()) != null) {
			line = line.trim();
			if(line.isEmpty()) {
				continue;
			}
			JSONObject tweetcont = (JSONObject)parser.parse(line);
			JSONObject user = (JSONObject)tweetcont.get("user");
			String user_id = user.get("id").toString();
			String tweet_id = tweetcont.get("id").toString();			
			int count_photo = 0;
			//boolean hasphoto = false;
			JSONObject entities = (JSONObject)tweetcont.get("entities");
			if(entities!=null){
				JSONArray media = (JSONArray)entities.get("media");
				if(media!=null){
					int media_len = media.size();
					for(int i=0; i < media_len; i++){	
						JSONObject med = (JSONObject)media.get(i);
						String type = med.get("type").toString();
						if(type!=null && type.equals("photo")){
							//hasphoto = true;
							count_photo = count_photo + 1;
						}
					}
				}
			}
//			if(hasphoto==true)
//				count_photo = 1;
//			else
//				count_photo = 0;
			out.println(user_id + "\t" + tweet_id+ "\t" + Integer.toString(count_photo));
		}		
		br.close();
	}
}
