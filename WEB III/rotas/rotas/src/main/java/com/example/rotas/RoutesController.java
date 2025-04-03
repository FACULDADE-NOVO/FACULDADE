package com.example.rotas;

import java.util.Optional;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
@RequestMapping("/routes")
public class RoutesController {

    @GetMapping("/data")
    @ResponseBody
    public String obtainData(){
        return "return some data";
        
    }

    @PostMapping("/create")
    @ResponseBody
    public String create(){
        return "create";

    }

    @GetMapping("/bebidas/{drinkType}")
    @ResponseBody
    public String drinkType(@PathVariable("drinkType") String drinkType){

        return "The drink chosen was: " + drinkType;

    }

    @GetMapping("/variables")
    @ResponseBody

    public String getURLVariables(@RequestParam Optional<String> category){

        return "The category chosen was: " + category.orElse("is null");
            
    }

    @PostMapping("/login")
    @ResponseBody

    public String getForm(@RequestParam String user, @RequestParam String password){

        return "user: " + user + " " +"password: " + password;
            
    }


    @GetMapping("/products")
    @ResponseBody

    public String getURLVariables(@RequestParam String product, @RequestParam Optional<String> category){

       return "The product chosen was: " + product; 
            
    }


}
