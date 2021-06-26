package server;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;

public class StringServer {
    private final ServerSocket server;
    public StringServer(int port) throws IOException {
        server = new ServerSocket(port);
    }

    private void connect() {

        while (true) {
            Socket socket = null;
            try {
                socket = server.accept();
                inout(socket);
            }

            catch (IOException e) {
                e.printStackTrace();
            } finally {
                if (socket != null)
                    try {
                        socket.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
            }
        }
    }

    private void inout(Socket socket) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintStream out = new PrintStream(socket.getOutputStream());
        String s;

        while(in.ready()) {
            s = in.readLine();
            out.println(s);
        }
    }

    public static void main(String[] args) throws IOException {
        StringServer server = new StringServer(3141);
        server.connect();


    }
}