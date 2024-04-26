import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;


public class Solution {
	

	private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        
        String binary = Integer.toBinaryString(n);
        String regex = "1";
        
        Pattern p = Pattern.compile(regex);
        Matcher m = p.matcher(binary);
        
        int count = 0;
        
        
        for (int j = 0; j < binary.length(); j++) {
        if (m.find()) {
        	count++;
        	
        	}
        
        }
        System.out.println(count);
        
        scanner.close();
    }
}
