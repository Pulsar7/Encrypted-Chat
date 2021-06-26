import java.io.*;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Random;


public class StringClient extends WrittenFile {

    public static String username () {
        String user = "#Gast";
        Random r = new Random();
        user += (r.nextInt(9999) + 1);

        return user;
    }

    public static int id () {
        Random r = new Random();
        int id = r.nextInt(9999) + 1;
        return id;
    }

    public static void main(String[] args) {
        Socket client = null;
        String s = username() + ", " +  id() + '\n';



        try {
            client = new Socket("localhost", 1337);
            OutputStream out = client.getOutputStream();
            DataOutputStream output = new DataOutputStream(out);
            output.writeUTF(s);


            InputStream rein = client.getInputStream();
            DataInputStream input = new DataInputStream(rein);
            String s1 = input.readUTF();

            while(s1.equals("ok")) {
                output.writeUTF(s);

            }
            client.close();



            System.out.println("available bytes: " + rein.available());
            BufferedReader buff = new BufferedReader(new InputStreamReader(rein));

            while (buff.ready()) {
                System.out.println(buff.readLine());
            }

        } catch (UnknownHostException e) {
            System.out.println("Unknown Host...");
            e.printStackTrace();
        } catch (IOException e) {
            System.out.println("IOProblems...");
            e.printStackTrace();
        } finally {
            if (client != null)
                try {
                    client.close();
                    System.out.println("Socket closed...");
                } catch (IOException e) {
                    System.out.println("not closing socket...");
                    e.printStackTrace();
                }
        }
    }
} 