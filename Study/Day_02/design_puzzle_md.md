# [과제] 디자인 패턴: 전략 패턴(Strategy Pattern)을 활용한 캐릭터 시스템 설계

## 1. 핵심 설계 원칙

* **변하는 부분**: WeaponBehavior
무기로 공격하는 행동.
* **변하지 않는 부분**: Character
캐릭터의 기본 속성, 무기장착과 공격 등의 기본 기능.
* **캡슐화**: WeaponBehavior를 캐릭터 클래스에서 분리하여 캡슐화합니다.

---

## 2. 클래스 정돈 및 역할

### 2.1 추상 클래스 (Abstract Class)
* **Character**: 모든 캐릭터 클래스의 최상위 부모 클래스입니다. setWeapon, fight 메서드를 포함합니다.

### 2.2 인터페이스 (Interface / ABC)
* **WeaponBehavior**: 무기 행동의 양식을 정의합니다.

### 2.3 일반 클래스 (Concrete Class)
* **캐릭터 종류**: `Queen`, `King`, `Knight`, `Troll`
* **무기 행동 종류**: `SwordBehavior`, `KnifeBehavior`, `AxeBehavior`, `BowAndArrowBehavior`

---

## 3. 클래스 관계 및 구조

* **상속 관계 (Inheritance)**:
`King`, `Queen`, `Knight`, `Troll` -> `Character`
* **구현 관계 (Implementation)**:
`SwordBehavior`, `KnifeBehavior`, `AxeBehavior`, `BowAndArrowBehavior`=> `WeaponBehavior`
* **구성 관계 (Composition)**:
`Character` 클래스는 `WeaponBehavior`타입의 인스턴스를 한개 가진다.

---

## 4. 메서드 구현
* **setWeapon(WeaponBehavior w)**: `Character` 클래스에 정의된 메서드로, 캐릭터의 무기를 실시간으로 교체합니다. 
* **fight()**: 각 캐릭터가 공격을 수행할 때 호출되는 메서드입니다. super()로 `weapon.useWeapon()`을 호출하여 구체적인 공격 행동을 위임(Delegate)합니다.