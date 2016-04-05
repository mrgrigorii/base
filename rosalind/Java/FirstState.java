package consolecalc;

import java.util.Scanner;

public class FirstState implements State {
	@SuppressWarnings("resource")
	public void doAction(Context context) {
	    System.out.println("Input first operand: ");
	    Scanner sc = new Scanner(System.in);
	    if(sc.hasNextDouble()) { 
	    	context.o1 = sc.nextDouble(); 
			System.out.println(context.o1);
	    } else {
	        System.out.println("Parse error. Use ',' not '.' Correct examples 45,5 , 43 ");
	        context.setState(new FirstState());
	        return;
	    }
		context.setState(new MidleState());
	}
}
