import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Start {
    public static void main(String[] args) throws IOException {
        System.setIn(Files.newInputStream(Paths.get(args[0])));
        System.setOut(new PrintStream(Files.newOutputStream(Paths.get(args[1]))));
        Main.main(null);
    }
}
