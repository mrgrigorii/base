package consolecalc;

public class RezultState implements State {
	public void doAction(Context context) {
	    System.out.print("Rezult: ");
	    System.out.print(context.o1);
	    System.out.print(context.operation);
	    System.out.print(context.o2);
	    System.out.print('=');
		
	    switch (context.operation) {
	    case '+':
	    	context.o1 = context.o1 + context.o2;
	    	System.out.println(context.o1);
	    	break;
	    case '-':
	    	context.o1 = context.o1 - context.o2;
	    	System.out.println(context.o1);
	    	break;
	    case '*':
	    	context.o1 = context.o1*context.o2;
	    	System.out.println(context.o1);
	    	break;
	    case '/':
	    	if (context.o2 == 0) {
	    		System.out.println(" Division by zero is forbidden.");
	    		break;
	    	} 	
	    	context.o1 = context.o1/context.o2;
	    	System.out.println(context.o1);
	    	break;
	    }
	    context.setState(new FirstState());
	}
}