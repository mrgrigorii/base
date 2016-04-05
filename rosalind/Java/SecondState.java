package consolecalc;

import java.util.Scanner;

public class SecondState implements State {
	public void doAction(Context context) {
	    System.out.println("Input second operand: ");
	    Scanner sc = new Scanner(System.in);
	    if(sc.hasNextDouble()) { 
	    	context.o2 = sc.nextDouble(); 
			System.out.println(context.o2);
	    } else {
	        System.out.println("Parse error. Use ',' not '.' Correct examples 45,5 , 43 ");
	        context.setState(new SecondState());
	        return;
	    }
	    context.setState(new RezultState());
	}

}
