import java.util.concurrent.TimeUnit;

public class DogDoor {
    private double height;  //in meter
    private boolean isOpen;
    private int autoCloseTime;   //in sec

    public DogDoor(int height, int autoCloseTime){
        this.height = height;
        this.autoCloseTime = autoCloseTime;
        this.isOpen = false;
    }

    public void closeDoor(){
        isOpen = false;
        System.out.println("door closed");
    }

    public void openDoor(){
        isOpen = true;
        System.out.println("door opened");
    }//have to delegate autoclose to remote. 
    //door should only handle pure open and close, in case there's need for perminant open

    public boolean checkIsOpen(){
        return isOpen;
    }

    public int getAutoCloseTime(){
        return autoCloseTime;
    }
    
}