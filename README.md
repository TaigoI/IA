# Questão 1
Implementação em questao1.py  
Base de conhecimento descrita no texto da questão está disponível em questao1.data  

Esta questão não pede resposta textual  

# Questão 2
Implementação em questao2.py  
Base de conhecimento descrita no texto da questão está disponível em questao2.data  
Programa em prolog está disponível em questao2.prolog

Comparando com uma implementação em prolog, é possível ver semelhanças e diferenças:
- A sintaxe em prolog é mais difícil, mas, é muito mais versátil.
- Prolog consegue partir da implicação para a regra. Ex.: sair de girafa(animal) para mamifero(animal)
- A comunicação com o usuário é mais fácil na minha implementação.
- A sintaxe é mais simples e próxima de expressões lógicas comuns na minha implementação.
- A sintaxe em Prolog é mais prolixa, por exemplo, eu preciso definir "pelo(_)" antes de dizer "mamifero(_) :- pelo(x)"

**Animais Adicionados nas Regras:**
```
Mamifero & Nada & TamanhoEnorme -> Baleia
Mamifero & Nada & TamanhoMedio -> Golfinho
!Ave & !Mamifero & Nada -> Peixe 
```

# Questão 3
