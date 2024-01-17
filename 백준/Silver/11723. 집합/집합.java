import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int X, result, num;
    static String cmd;
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        X = Integer.parseInt(br.readLine());

        for (int i = 0; i < X; i++) {
            st = new StringTokenizer(br.readLine());
            cmd = st.nextToken();

            if (!(cmd.equals("all") || cmd.equals("empty"))) {
                num = Integer.parseInt(st.nextToken());
            }

            if (cmd.equals("add")) {
                result |= (1 << num);
            } else if (cmd.equals("remove")) {
                result &= ~(1 << num);
            } else if (cmd.equals("check")) {
                if ((result & (1 << num)) > 0) {
                    sb.append("1").append("\n");
                } else {
                    sb.append("0").append("\n");
                }
            } else if (cmd.equals("toggle")) {
                result ^= (1 << num);
            } else if (cmd.equals("all")) {
                result = -1;
            } else if (cmd.equals("empty")) {
                result = 0;
            }
        }
        System.out.println(sb.toString());
    }
}