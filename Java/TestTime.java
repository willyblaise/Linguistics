// Java program to demonstrate
// working of TimerTask class
import java.util.Timer;
import java.util.TimerTask;

class Helper extends TimerTask
{
	public static int i = 0;
	public void run()
	{
		System.out.println("Timer ran" + ++i);
		if(i == 10)
		{
			synchronized(TestTime.obj2)
			{
				TestTime.obj2.notify();
			}
		}
	}
	
}


public class TestTime
{
	public static TestTime obj2;
	public static void main(String[] args) throws InterruptedException
	{
		obj2 = new TestTime();
		
		// creating an instance of timer class
		Timer timer = new Timer();
		
		// creating an instance of task to be scheduled
		TimerTask task = new Helper();
		
		// scheduling the timer instance
		timer.schedule(task, 5000, 3000);
		
		// fetching the scheduled execution time of
		// the most recent actual execution of the task
		System.out.println(task.scheduledExecutionTime());

		synchronized(obj2)
		{
            System.out.println("What the hell");
			//this thread waits until i reaches 4
			obj2.wait();
		}
        System.out.println("What the hell last");

		//canceling the task assigned
		System.out.println("Cancel the timer task: " + task.cancel());

		// at this point timer is still running
		// without any task assigned to it
	
		// canceling the timer instance created
		timer.cancel();
	}
}
