package consolecalc;

import java.io.IOException;

public class ConsoleCalcApp {
	public static void main(String[] args) throws IOException {
		System.out.println("Welcome, I'm a simple calculator.");
		Context context = new Context();
		while (true) {
			context.getState().doAction(context);
		}
	}
}