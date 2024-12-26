public class GuitarSpec{
    private Type type;
    private Builder builder;
    private int numString;

    public GuitarSpec(Builder builder, Type type, int numString){
        this.type = type;
        this.builder = builder;
        this.numString = numString;
    }

    public int getNumString() {
        return numString;
    }

    public String getType() {
        return type.toString();
    }

    public String getBuilder(){
        return builder.toString();
    }


    public boolean matches(GuitarSpec otherSpec){
        if(builder != otherSpec.builder)
            return false;
        if(type != otherSpec.type)
            return false;
        if(numString != otherSpec.numString)
            return false;

        return true;
    }
}