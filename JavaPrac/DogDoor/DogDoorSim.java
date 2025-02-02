import java.lang.Thread;
public class DogDoorSim {

    public static void main(String[] args){
        DogDoor door = new DogDoor(1, 1);
        Remote remote = new Remote(door);
        System.out.println("Fibo barks");
        remote.pressButton();
        System.out.println("Fibo goes out");
        
        try {
            for(int i=0; i<3; i++){
                System.out.println(".");
                Thread.sleep(3000);

            }
            
        } catch (Exception e) {
            // TODO: handle exception
        }

        System.out.println("fibo done, bark again");
        remote.pressButton();
        System.out.println("fibo comes inside");


    }
}