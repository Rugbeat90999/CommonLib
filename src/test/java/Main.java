import net.anonhub.commonlib.ConfigParser;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import static net.anonhub.commonlib.ConfigParser.DATA_TYPE_CHAR;

public class Main {
    public static final Path basePath = Paths.get("./resources");

    public static void main(String[] args) throws IOException {
        HashMap<String, HashMap<String, ArrayList<String>>> map = new HashMap<>();
        map.put("version", new HashMap<>());
        map.put("tickSpeed", new HashMap<>());
        map.put("difficulty", new HashMap<>());
        map.put("actions", new HashMap<>());

        map.get("version").put("current", new ArrayList<>(List.of("0.0.1")));
        map.get("version").put("current"+DATA_TYPE_CHAR, new ArrayList<>(List.of("String")));

        map.get("tickSpeed").put("default", new ArrayList<>(List.of("20")));
        map.get("tickSpeed").put("default"+DATA_TYPE_CHAR, new ArrayList<>(List.of("byte")));
        map.get("tickSpeed").put("current", new ArrayList<>(List.of("20")));
        map.get("tickSpeed").put("current"+DATA_TYPE_CHAR, new ArrayList<>(List.of("byte")));

        map.get("difficulty").put("max", new ArrayList<>(List.of("100")));
        map.get("difficulty").put("max"+DATA_TYPE_CHAR, new ArrayList<>(List.of("byte")));
        map.get("difficulty").put("min", new ArrayList<>(List.of("10")));
        map.get("difficulty").put("min"+DATA_TYPE_CHAR, new ArrayList<>(List.of("byte")));
        map.get("difficulty").put("default", new ArrayList<>(List.of("25")));
        map.get("difficulty").put("default"+DATA_TYPE_CHAR, new ArrayList<>(List.of("byte")));
        map.get("difficulty").put("current", new ArrayList<>(List.of("100")));
        map.get("difficulty").put("current"+DATA_TYPE_CHAR, new ArrayList<>(List.of("byte")));

        map.get("actions").put("openTerminal", new ArrayList<>(List.of("66")));
        map.get("actions").put("openTerminal"+DATA_TYPE_CHAR, new ArrayList<>(List.of("short")));
        map.get("actions").put("exit", new ArrayList<>(List.of("111")));
        map.get("actions").put("exit"+DATA_TYPE_CHAR, new ArrayList<>(List.of("short")));
        map.get("actions").put("quit", new ArrayList<>(List.of("111")));
        map.get("actions").put("quit"+DATA_TYPE_CHAR, new ArrayList<>(List.of("short")));
        map.get("actions").put("moveUp", new ArrayList<>(List.of("51", "19")));
        map.get("actions").put("moveUp"+DATA_TYPE_CHAR, new ArrayList<>(List.of("short", "short")));
        map.get("actions").put("moveDown", new ArrayList<>(List.of("47", "20")));
        map.get("actions").put("moveDown"+DATA_TYPE_CHAR, new ArrayList<>(List.of("short", "short")));
        map.get("actions").put("moveLeft", new ArrayList<>(List.of("29", "21")));
        map.get("actions").put("moveLeft"+DATA_TYPE_CHAR, new ArrayList<>(List.of("short", "short")));
        map.get("actions").put("MoveRight", new ArrayList<>(List.of("32", "22")));
        map.get("actions").put("MoveRight"+DATA_TYPE_CHAR, new ArrayList<>(List.of("short", "short")));
        map.get("actions").put("sprint", new ArrayList<>(List.of("59", "60")));
        map.get("actions").put("sprint"+DATA_TYPE_CHAR, new ArrayList<>(List.of("short", "short")));

        ConfigParser parser = new ConfigParser(basePath+"/assets/.cfg", map);
//        System.out.println("path: "+basePath);
//        System.out.println("Parser: "+parser);
    }
}
