package br.edu.ifpr.foz.projeto_spring;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import jakarta.servlet.http.HttpServletRequest;

@Controller
@RequestMapping("/greetings")
public class GreetingsController {

    @GetMapping("")
    @ResponseBody
    public String greetings(){
        return "Greetins! Welcome to the Spring Project";
    }

    @GetMapping("/headers")
    @ResponseBody
    public String getRequestHeaders(HttpServletRequest request){

        String userAgent = request.getHeader("User-agent");

        return "<h1>" + userAgent + "<h1>";

    }

    @GetMapping("/user-agent")
    @ResponseBody
    public void userAgent(@RequestHeader("User-Agent") String userAgent){

        System.out.println("User-Agent" + userAgent);


    }
    
}
