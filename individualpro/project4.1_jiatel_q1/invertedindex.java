package project41;
import java.io.File;
import java.io.IOException;
import java.util.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

public class invertedindex {
	public static class Map extends Mapper<LongWritable, Text, Text, Text> {
		private Text word = new Text();
		
		public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
			String line = value.toString();
			line = line.replaceAll("\\p{P}", " ").toLowerCase();//replace all punctuation with blank
			StringTokenizer tokenizer = new StringTokenizer(line);
			FileSplit fs = (FileSplit)context.getInputSplit();
			String location = fs.getPath().getName();
			Text locate = new Text(location);
			while (tokenizer.hasMoreTokens()) {
				word.set(tokenizer.nextToken());
				context.write(word, locate);
			}
		}
	}
	public static class Reduce extends Reducer<Text, Text, Text, Text> {
		 public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
			 Set<Text> fileset = new HashSet<Text>();
			 boolean isfirst = true;
			 StringBuffer filenameset = new StringBuffer();
			 filenameset.append(": ");
			 for (Text val : values) {
				 if(!fileset.contains(val)){
					 fileset.add(val);
					 String filename = val.toString();
					 if(!isfirst){
						 filenameset.append(" ");
						 filenameset.append(filename);
					 }
					 else{
						 filenameset.append(filename);//record file name that has already appeared
					 }
					 isfirst = false;
				 }
			 }
			 isfirst = true;
			 Text fileout = new Text(filenameset.toString());
			 context.write(key, new Text(fileout));
		 }
	}
	
	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		Job job = new Job(conf, "invertedindex");
		job.setJarByClass(invertedindex.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);

		job.setMapperClass(Map.class);
		job.setReducerClass(Reduce.class);

		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);

		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));

		job.waitForCompletion(true);
	}
}
