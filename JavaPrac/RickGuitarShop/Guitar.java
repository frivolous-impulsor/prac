public class Guitar{
    private float price;
    private String SN;
    private GuitarSpec guitarSpec;

    public Guitar(float price, String SN, GuitarSpec guitarSpec){
        this.price = price;
        this.SN = SN;
        this.guitarSpec = guitarSpec;
    }

    public float getPrice(){
        return price;
    }

    public String getSN(){
        return SN;
    }

    public GuitarSpec getGuitarSpec(){
        return guitarSpec;
    }

    
}