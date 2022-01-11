import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        while(sc.hasNextLine()){
            String[] text = sc.nextLine().split(" ");
            int a = Integer.parseInt(text[0]);
            int b = Integer.parseInt(text[1]);
            System.out.println(a+b);
        }
    }
}
