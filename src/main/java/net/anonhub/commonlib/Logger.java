package net.anonhub.commonlib;

import java.io.*;
import java.time.LocalTime;

public class Logger {
    private final File file;
    private final BufferedWriter writer;

    public Logger(String filePath) throws IOException {
        file = new File(filePath);
        if (file.createNewFile()) {
            System.out.println("New log file made");
        } else {
            System.out.println("Log file found");
        }
        writer = new BufferedWriter(new FileWriter(file, true));
    }

    public void log(Object textObject) {
        String now = LocalTime.now().toString().substring(0, 11);
        // Print to console
        System.out.println("[" + now + "] " + textObject.toString());

        // Append to file
        try {
            writer.write("[" + now + "] " + textObject);
            writer.newLine();
        } catch (IOException e) {
            System.err.println("Failed to write to log file: " + e.getMessage());
        }
    }
}
