import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws Exception {
		String str = br.readLine(); // 입력을 받음
		
		str= str.replace("apa", "a"); // 만약에 apa가 있다면 a가 apa가 된것이다. apa를 찾아서 a로 바꿔준다.
		str= str.replace("epe", "e");// 만약에 epe가 있다면 e가 apa가 된것이다. epe를 찾아서 e로 바꿔준다.
		str= str.replace("ipi", "i");// 만약에 ipi가 있다면 i가 apa가 된것이다. ipi를 찾아서 i로 바꿔준다.
		str= str.replace("opo", "o");// 만약에 opo가 있다면 o가 apa가 된것이다. opo를 찾아서 o로 바꿔준다.
		str= str.replace("upu", "u");// 만약에 upu가 있다면 u가 apa가 된것이다. upu를 찾아서 u로 바꿔준다.
		System.out.println(str); // 정답 출력 
		
	}

}
