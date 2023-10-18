6.1. Найдите кпопку c текстом "Gold". Попробуйте подобрать как минимум 2 разных XPATH и/или CSS-селекторов
http://suninjuly.github.io/xpath_examples
### CSS
```
.bg-light > :nth-child(2) :nth-child(3)
.bg-light > :nth-last-child(1) :nth-last-child(2)
.bg-light > :nth-child(2) :nth-last-child(2)
```
### XPath
```
/html/body/div[2]/button[3]
//div[2]/button[3]
/html/body/div[last()]/button[last()-1]
//div[last()]/button[last()-1]
//button[text() = 'Gold']
 ```
 ***
6.2. Найдите элемент с текстом "Fully charged cat". Чем больше разных XPATH и/или CSS-селекторов сможете подобрать, тем лучше
http://suninjuly.github.io/cats.html
### CSS
 ```
 body > main > div > div > div > div:nth-child(5) > div > div > p
.row :nth-child(5) .card-text

 ```
### XPath
 ```
//html/body/main/div/div/div/div[5]/div/div/p
//p[text() = 'Fully charged cat']
 ```
