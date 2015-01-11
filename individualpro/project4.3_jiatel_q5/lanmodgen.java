package project43;


import java.io.File;
import java.io.IOException;
import java.util.*;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
import org.apache.hadoop.hbase.mapreduce.TableMapReduceUtil;
import org.apache.hadoop.hbase.util.Bytes;
import org.apache.hadoop.hbase.mapreduce.TableReducer;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

import project43.myPair;

class myPair<K extends Comparable<K>, V extends Comparable<V>> implements Comparable<myPair<K, V>> {
	K key;
	V value;
	public myPair(K key, V value) {
		this.key = key;
		this.value = value;
	}
	public V getValue() {
		return value;
	}
	public K getKey() {
		return key;
	}
	public int compareTo(myPair<K, V> pair) {
		return -value.compareTo(pair.getValue());
	}
}


public class lanmodgen {
	public static Configuration conf = HBaseConfiguration.create();	
	public static class Map extends Mapper<LongWritable, Text, Text, Text> {
		private Text outword = new Text();
		private Text outword1 = new Text();
		int threshold_t = 2;
		String words = "";
		String count = "";
		String pre_word = "";
		String next_word = "";
		int tem_index = 0;
		public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
			String line = value.toString();
			String linecon[] = line.split("\t");
			words = linecon[0];//the whole words
			count = linecon[1];//its count
			String wordsp[] = words.split(" ");
			if(wordsp.length >= threshold_t){//set the threshold, 2 should be the parameter which could be set
				tem_index = words.lastIndexOf(" ");//index of the last " "
				pre_word = words.substring(0, tem_index);
				next_word = words.substring(tem_index+1);
				outword.set(pre_word);
				outword1.set(next_word + "\t" + count);
				context.write(outword,outword1);
			}
		}
	}
	public static class Reduce extends TableReducer<Text, Text, ImmutableBytesWritable> {
		String re_word = "";
		int re_count = 0;
		int threshold_n = 5;
		 public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
	         SortedSet<myPair<String, Integer>> word_set = new TreeSet<myPair<String, Integer>>();
			 int sumcount = 0;//record the sum of all counts
			 for (Text val : values) {
				String content[] = val.toString().split("\t");
				re_word = content[0];//the next word
				re_count = Integer.parseInt(content[1]);//its count
				word_set.add(new myPair<String, Integer>(re_word, re_count));
				sumcount = sumcount + re_count;
			 }
			 
			 Put put = new Put(Bytes.toBytes(key.toString()));
			 double Probability = 0;//probability of each word
	         int i = 0;
	         Iterator it= word_set.iterator();
	         while (i < threshold_n && it.hasNext()) {
	        	 myPair en = (myPair)it.next();
	        	 String new_word = (String)en.getKey();
	        	 int new_count = (int)en.getValue();
	        	 Probability = new_count * 100.0 / sumcount;
	        	 put.add(Bytes.toBytes("Probability"),
	        			 Bytes.toBytes(new_word),
	        			 Bytes.toBytes("" + Probability));
	                i++;
	            }
	         
			 
	         if(!put.isEmpty()) {
	            	context.write(new ImmutableBytesWritable(key.getBytes()), put);
	            }
		 }
	}
	
	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		Job job = new Job(conf, "project43");

		job.setJarByClass(lanmodgen.class);

		TableMapReduceUtil.initTableReducerJob("project43", // output table
				Reduce.class, // reducer class
				job);
		TableMapReduceUtil.addDependencyJars(job);
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(Text.class);


		job.setMapperClass(Map.class);
		job.setReducerClass(Reduce.class);

		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);
		conf.set("threshold_t", args[3]);
		conf.set("threshold_n", args[4]);
		FileInputFormat.addInputPath(job, new Path(args[1]));
		FileOutputFormat.setOutputPath(job, new Path(args[2]));

		job.waitForCompletion(true);
	}
}
