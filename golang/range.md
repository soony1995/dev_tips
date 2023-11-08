## range 

> range 는 일반적으로 for 문과 같이 쓰인다. 

```go
sl := []string{}
str := "안녕하세요"
mapValue := make(map[string]string,3)
ch := make(chan error, 1)

for i,v := range v {
    ... 
}
```

위의 코드 처럼 슬라이스,맵,채널 등이 올 수 있다.

range 뒤에 오는 표현식은 루프가 시작 될 때 딱 한번 평가 된다. 따라서 이후에 바꾼다고 한들 변하지 않는다.

### 문제 발생 경우
> go func()을 이용해서 for문을 사용할 때 문제가 발생했다.

```go
func foobyval(n int) {
  fmt.Println(n)
}

func main() {
  for i := 0; i < 5; i++ {
    go foobyval(i)
  }

  time.Sleep(100 * time.Millisecond)
}
```
```
output: 
0
1
2
3
4
```
```go
func foobyref(n *int) {
  fmt.Println(*n)
}

func main() {
  for i := 0; i < 5; i++ {
    go foobyref(&i)
  }

  time.Sleep(100 * time.Millisecond)
}
```
```
output: 
5
5
5
5
```

이런 결과가 나타나는 이유는 i는 하나의 주소값을 가진 객체이며 각 반복마다 새로운 객체가 아니기 때문이다.

```
func main() {
	for i := 0; i < 5; i++ {
		fmt.Println(&i)
	}
}
output: 
0xc000118000
0xc000118000
0xc000118000
0xc000118000
0xc000118000
```