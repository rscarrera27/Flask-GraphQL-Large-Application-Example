#  ✨✨Awesome-GraphQL✨✨

## Summary
GraphQL tutorial and server template with Python


## GraphQL
GraphQL은 페이스북에서 개발한 어플리케이션 레이어 쿼리 언어이다. GraphQL을 사용하면 서버의 구조를 간단히 하고 클라이언트는 서버의 API 추가 없이도 원하는 형태로 쿼리하여 데이터를 받아올수 있게 된다. 간단히 말하면 서버에 쿼리를 사용하여 데이터를 받아올수 있다고 생각하면 된다.

### GraphQL의 쿼리와 뮤테이션
REST API를 사용하면 GET 요청을 통해 데이터를 받아오고 PUT과 POST를 사용하여 데이터를 변경 및 추가한다. GraphQL또한 데이터 가져오기와 데이터 변경 기능을 가지고 있다. GraphQL에서는 데이터 가져오기를 쿼리, 데이터 변경하기를 뮤테이션이라고 한다. 

GraphQL의 가장 큰 장점은 쿼리이기 때문에 먼저 쿼리에 대하여 알아보자 

#### Query

##### 1.필드

기본적인 GraphQL 쿼리는 다음과 같이 객체의 특정 필드를 요청하는 것이다.

**쿼리**
```
{
  hero {
    name
  }
}
```
**응답**
```json
{
  "data": {
    "hero": {
      "name": "R2-D2"
    }
  }
}
```

쿼리를 작성한대로 쿼리가 돌아오는 것을 알 수 있다. 

앞선 예제에서는 문자열 필드를 받아왔지만 GraphQL은 객체를 비롯한 다양한 필드를 반환 할수도 있다.
```
{
  hero {
    name
    friends {
      name
    }
  }
}
```
```json
{
  "data": {
    "hero": {
      "name": "R2-D2",
      "friends": [
        {
          "name": "Luke"
        },
        {
          "name": "Leia"
        }
      ]
    }
  }
}
```

##### 2. 인수

필드에 대한 기본적인 예제에서는 전체 도큐먼트에서 해당 필드를 가져왔다.
그러나 인수를 사용한다면 해당하는 조건의 도큐먼트의 필드만 가져올 수 있다.

다음은 id가 1000인 사람의 이름과 키를 가져오는 쿼리이다.

**요청**
```
{
  human(id: 1000) {
    name
    height
  }
}
```
**응답**
```json
{
  "data": {
    "human":{
      "name": "Luke",
      "height": 1.72
    }
  }
}
```

또한 각 필드에 인수를 전달하여 서버에서 데이터 변환을 수행하도록 할 수 있습니다.

**요청**
```
{
  human(id: 1000) {
    name
    height(unit: FOOT)
  }
}
```
**응답**
```json
{
  "data": {
    "human":{
      "name": "Luke",
      "height": 5.6430448
    }
  }
}
```

##### 별칭(Aliases)
쿼리에 별칭을 사용하여 필드의 결과를 바꿀 수 있다. 또한 GraphQL의 쿼리를 작성할때는 한 쿼리에 다른 인수를 사용하여 같은 필드를 여러번 요청할수 없지만 별칭을 사용하여 같은 필드를 다른 이름으로 여러번 받아올 수 있다.

**요청**
```
{
  empireHero: Hero(EPISODE: EMPIRE){
    name
  }
  jediHero: Hero(EPISODE: JEDI) {
    name
  }
}
```
**응답**
```json
{
  "data": {
    "empireHero": {
      "name": "Luke Skywalker"
    },
    "jediHero": {
      "name": "R2-D2"
    }
  }
}
```

##### 조각(Fragments)
쿼리를 복잡하게 짜다 보면 같은 구성의 필드들을 여러번 사용하는 경우가 있는데 이럴때 조각을 사용해서 좀 더 간단하게 만들수 있다. 예를 들면 주인공 두명을 비교하고자 할 떄 주인공에 대한 같은 필드를 두번 반복할 필요 없이 필드를 조각으로 묶어서 재사용할 수 있다. 

필드를 담고 있는 일종의 변수라고 생각히면 된다. 동일한 타입의 조각끼리 사용할 수 있다.

다음 예시는  Hero 필드를 각기 다른 인수로 조회한 것을 조각으로 만들고 이 조각을 사용해서 두 Hero를 한번에 출력하는 예시이다.
**요청**
```
{
  empireHero: Hero(EPISODE: EMPIRE){
    ...fragFields
  }
  jediHero: Hero(EPISODE: JEDI) {
    ...fragFields
  }
}

fragment fragFields on Character {
  name
  friends {
    name
  }
}
```
**응답**
```json
{
  "data": {
    "empireHero": {
      "name": "Luke Skywalker",
      "friends": {
        "Han Solo"
      }
    },
    "jediHero": {
      "name": "R2-D2",
      "friends": {
        "C3PO"
      }
    }
  }
}
```

##### 작업 이름(Operation Name)

지금까지는 쿼리 앞에 작업 유형 키워드와 작업 이름을 생략했다. 그러나 쿼리나 뮤테이션과 같은 작업 유형 키워드와 작업 이름을 지정하면 디버깅 및 로깅이 쉬워지며 이름으로 찾기 때문에 문제가 있는 쿼리를 찾기 쉬워진다. 

함수를 선언한다고 생각하면 편하다.

**요청**
```
query HumanNameAndHeight{
  human(id: 1000) {
    name
    height(unit: FOOT)
  }
}
```

**응답**
```json
{
  "data": {
    "human":{
      "name": "Luke",
      "height": 5.6430448
    }
  }
}
```

##### 변수
지금까지는 모든 인수를 쿼리 안에 작성하지만 애플리케이션을 작성할때는 보통 대부분 동적으로 인수를 사용하기 원한다. 쿼리를 동적으로 생성하는 방법도 있겠지만 GraphQL은 변수를 다른 JSON으로 전달하고 쿼리 안에서 이 변수를 사용할 수 있는 더 좋은 방법을 제공한다.

다음은 변수를 사용하여 쿼리를 작성하는 예시이다. ``$`` 기호로 변수를 선언하고 타입을 지정한 후 변수를 쿼리에 인자 부분에 전달한다. 변수의 내용은 쿼리 변수 JSON에서 ``변수 이름: 변수 내용`` 형식으로 따로 전달한다. 

함수를 만들고 인수를 전달해 쿼리한다고 생각하면 편하다.

**요청**
```
query HumanNameAndHeight($id: Int){
  human(id: $id) {
    name
    height
  }
}
```
**쿼리 변수**
```json
{
  "id": 1000
}
```

**응답**
```json
{
  "data": {
    "human":{
      "name": "Luke",
      "height": 1.72
    }
  }
}
```

또한 다음과 같이 기본값을 지정할 수도 있다.
```
query HumanNameAndHeight($id: Int=1000){
  human(id: $id) {
    name
    height
  }
}
```
