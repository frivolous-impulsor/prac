import java.util.Iterator;
import java.util.List;

public class FindGuitarTester {

    public static void main(String[] args) {
        Inventory guitarShop = new Inventory();
        initalizeInventory(guitarShop);

        GuitarSpec erinWants = new GuitarSpec(Builder.MARTIN, Type.ACOUSTIC, 12);

        List matchingGuitars = guitarShop.search(erinWants);
        if(matchingGuitars.isEmpty()){
            System.out.println("sorry Eerin, we got nothing for you");
        }else{
            System.out.println("Hey Erin, we got something for you!");
            for(Iterator i = matchingGuitars.iterator(); i.hasNext();){
                Guitar guitar = (Guitar)i.next();
                System.out.println("we have a " + 
                    guitar.getGuitarSpec().getBuilder() + " " +
                    guitar.getGuitarSpec().getType() + " with price "+
                    guitar.getPrice());
            }
        }


    }


    private static void initalizeInventory(Inventory inventory){
        GuitarSpec spec1 = new GuitarSpec(Builder.MARTIN, Type.ACOUSTIC, 12);
        inventory.addGuitar("SFNNX", 11.9f, spec1);

        GuitarSpec spec2 = new GuitarSpec(Builder.GIBSON, Type.ELECTRIC, 12);
        inventory.addGuitar("SFMSB", 15.8f, spec2);
    }
}