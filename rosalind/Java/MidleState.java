package consolecalc;

import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

public class MidleState implements State {
	private Set<Character> test;
	public MidleState(){
		this.test = new HashSet<Character>();
		this.test.add('+');
		this.test.add('-');
		this.test.add('*');
		this.test.add('/');
	}
	public void doAction(Context context) {
		char ignore;
		System.out.println("Input operation: ");		
		try {
			context.operation = (char) System.in.read();
			do {
				ignore = (char) System.in.read();
			} while (ignore != '\n');
		} catch (IOException e) {
			// TODO Auto-generated catch block
			System.out.println("Wrong operand, must be +,-,* or /");
			context.setState(new MidleState());
			e.printStackTrace();
		}
		if (!this.test.contains(context.operation)) {
			System.out.print("Wrong operand, should be ");
			System.out.println(this.test.toString());
			context.setState(new MidleState());
		}
		else {
			context.setState(new SecondState());
		}
	}		
}

