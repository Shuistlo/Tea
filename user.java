public class User{
    private String[] trueMoods = ["happy", "sad", "stressed", "irritable", "neutral", "angry"];
    private String[] trueWeathers = ["cold", "rainy", "snowy", "hot", "sunny", ]; //should there be humid?
    private String[] trueActivities = ["exercised", "traveling", "had sugar", "sick", "slept badly", "slept well"];
    private String[] trueBodies = ["fatigue", "headache", "nausea", "dizziness"];

    private String mood;
    private String weather;
    private String activity;
    private String body;
    //need a way of storing this data

    //this person's tea data
    //i need some way of associating people's tea preferences with the above factors ^ (mood, weather, activity, body)

    Person(){

    }

    public String getMood() {
        return mood;
    }

    public void setMood(String mood) {
        this.mood = mood;
    }

    public String getWeather() {
        return weather;
    }

    public void setWeather(String weather) {
        this.weather = weather;
    }

    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
}