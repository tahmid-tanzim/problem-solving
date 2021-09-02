import java.util.*;

class Person {
	protected String firstName;
	protected String lastName;
	protected int idNumber;
	
	// Constructor
	Person(String firstName, String lastName, int identification){
		this.firstName = firstName;
		this.lastName = lastName;
		this.idNumber = identification;
	}
	
	// Print person data
	public void printPerson(){
		 System.out.println(
				"Name: " + lastName + ", " + firstName 
			+ 	"\nID: " + idNumber); 
	}
	 
}

class Student extends Person{
	private int[] testScores;

    /*	
    *   Class Constructor
    *   
    *   @param firstName - A string denoting the Person's first name.
    *   @param lastName - A string denoting the Person's last name.
    *   @param id - An integer denoting the Person's ID number.
    *   @param scores - An array of integers denoting the Person's test scores.
    */
	// Constructor
	Student(String firstName, String lastName, int identification, int[] testScores){
		super(firstName, lastName, identification);
        this.testScores = testScores;
	}

    /*	
    *   Method Name: calculate
    *   @return A character denoting the grade.
    */
    public char calculate() {
        int sum = 0, len = this.testScores.length;
        for(int i = 0; i < len; i++) {
            sum += this.testScores[i];
        }

        float avg = (float) sum / len;
        char l;
        if(avg >= 90.0 && avg <= 100.0) {
            l = 'O';
        } else if(avg >= 80.0 && avg < 90.0) {
            l = 'E';
        } else if(avg >= 70.0 && avg < 80.0) {
            l = 'A';
        } else if(avg >= 55.0 && avg < 70.0) {
            l = 'P';
        } else if(avg >= 40.0 && avg < 55.0) {
            l = 'D';
        } else if(avg < 40.0) {
            l = 'T';
        }

        return l;
    }
}

public class Inheritance {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
		String firstName = scan.next();
		String lastName = scan.next();
		int id = scan.nextInt();
		int numScores = scan.nextInt();
		int[] testScores = new int[numScores];
		for(int i = 0; i < numScores; i++){
			testScores[i] = scan.nextInt();
		}
		scan.close();
		
		Student s = new Student(firstName, lastName, id, testScores);
		s.printPerson();
		System.out.println("Grade: " + s.calculate());
    }
}
