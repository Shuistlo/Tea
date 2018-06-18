public class Tea{
    private static final String[] trueToppings = []; //list of toppings

    private String teaBase;
    private int size;
    private String[] toppings;
    private double sugarAmount;
    private String temperature;
    private boolean milk;

    //going to need some way of not being able to costruct if teabase does not exist
    Tea(String nteaBase, int nsize, String[] ntoppings, boolean nmilk, double nsugarAmount, String ntemperature){
        this.teaBase = nteaBase;
        this.size = nsize;
        this.toppings = ntoppings;
        this.milk = nmilk;
        this.sugarAmount = nsugarAmount;
        this.temperature = ntemperature;
    }

    public String getTeaBase() {
        return teaBase;
    }

    public void setTeaBase(String teaBase) {
        this.teaBase = teaBase;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public String[] getToppings() {
        return toppings;
    }

    public void setToppings(String[] toppings) {
        this.toppings = toppings;
    }

    public double getSugarAmount() {
        return sugarAmount;
    }

    public void setSugarAmount(double sugarAmount) {
        this.sugarAmount = sugarAmount;
    }

    public String getTemperature() {
        return temperature;
    }

    public void setTemperature(String temperature) {
        this.temperature = temperature;
    }

    //will need another toString this is just a teabase
    public String toString(){
        StringBuilder sb = new StringBuilder("A lovely ");
        sb.append(size);
        sb.append(" oz cup of tea made with");
        sb.append(teaBase);
        sb.append(".");
        String tString = sb.toString();
        return tString;
    }
}