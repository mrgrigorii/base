/**
 * 
 */
package consolecalc;
import java.util.Scanner;
import java.util.regex.Matcher;  
import java.util.regex.Pattern; 
/**
 * @author Grigory Kovtun 
 *
 */
public class ÑonsoleÑalc {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ÑonsoleÑalc A = new ÑonsoleÑalc();
		//A.parse();
		//Scanner scan = new Scanner(System.in);
		//String s = scan.nextLine();
		//System.out.println(s);
		Pattern p = Pattern.compile("([0-9]+)([+*-/])([0-9]+)");  
        Matcher m = p.matcher(A.parse());
        System.out.println( m.matches());
        System.out.println("123"+"+890");

	}
	
	@SuppressWarnings("resource")
	public String parse() {
		Scanner sc = new Scanner(System.in); 
		String s;
		System.out.print("Ââåäèòå âûğàæåíèå: ");
		if(sc.hasNextLine()) { 
			s = sc.nextLine(); 
			System.out.println(s);
			return s;
	    } else {
	        System.out.println("Error");
	        return null;
	    }
	}

}
