import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class Inventory {

    private List guitars;

    public Inventory() {
        guitars = new LinkedList();
    }

    public void addGuitar(String SN, float price, GuitarSpec guitarSpec){
        Guitar guitar = new Guitar(price, SN, guitarSpec);
        guitars.add(guitar);
    }

    public Guitar getGuitar(String SN){
        for(Iterator i = guitars.iterator(); i.hasNext();){
            Guitar guitar = (Guitar)i.next();
            if(guitar.getSN().equals(SN)){
                return guitar;
            }
        }
        return null;
    }

    public List search(GuitarSpec searchSpec){
        List matchingGuitars = new LinkedList();
        for (Iterator i = guitars.iterator(); i.hasNext();){
            Guitar guitar = (Guitar)i.next();
            if(guitar.getGuitarSpec().matches(searchSpec)){
                matchingGuitars.add(guitar);
            }
        }
        return matchingGuitars;
    }
}