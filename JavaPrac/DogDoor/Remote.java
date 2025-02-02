import java.util.Timer;
import java.util.TimerTask;

public class Remote {

    private DogDoor door;

    public Remote(DogDoor door){
        this.door = door;
    }

    public void pressButton(){
        boolean isOpen = door.checkIsOpen();
        if(isOpen){
            door.closeDoor();
        }else{
            door.openDoor();
            int autoCloseTime = door.getAutoCloseTime();

            //auto close
            final Timer timer = new Timer();
            timer.schedule(
                new TimerTask() {
                    public void run(){
                        door.closeDoor();
                        timer.cancel();
                    }
                }
            , autoCloseTime*1000);
        }
    }
}