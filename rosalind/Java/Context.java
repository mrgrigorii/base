package consolecalc;

public class Context {
	private State state;
	public double o1;
	public double o2;
	public char operation;

	public Context(){
		state =  new FirstState();
	}

	public void setState(State state){
		this.state = state;		
	}

	public State getState(){
	    return state;
	}
}
