# Qubit (큐비트)
$$\ket{\psi}=\alpha \ket 0 + \beta \ket 1 \quad\quad \cdots \ (1)$$
와 같은 형태로 표현할 수 있음
위 식은 
$$\ket\psi = e^{i\gamma} \left(\cos\frac{\theta}{2}\ket{0} + e^{i\varphi}\sin\frac{\theta}{2}\ket{1}\right)$$
의 형태로 표현할 수 있음 
	$\theta, \varphi, \gamma$는 실수
	$e^{i\gamma}$는 무시할 수 있음
$$i.e. \ket\psi =\cos\frac{\theta}{2}\ket{0} + e^{i\varphi}\sin\frac{\theta}{2}\ket{1}$$
$\theta, \varphi$는 3차원 단위 구(Bloch Sphere, 블로흐 구) 위의 한 점을 정의

# Superposition (중첩)
큐비트가 $\ket{0}$과 $\ket{1}$인 계산기저상태가 아닌 이 둘의 선형조합 상태를 형성하는 것
$$\text{ex)}\quad\quad \frac{1}{\sqrt 2}\ket{0}+\frac{1}{\sqrt 2}\ket{1}$$

# Hilbert Space (힐베르트 공간)
유한차원의 복소벡터공간에서 내적공간
## 내적공간
### 내적
어떤 벡터공간의 두 벡터 $\ket{v}$와 $\ket{w}$를 입력 받아 복소수를 출력하는 함수
$\ket{v}$와 $\ket{w}$는 내적공간에 속한 벡터들이며, $\ket{v}$ 벡터의 쌍대벡터(dual vector)는 $\bra{v}$로 표기함
	쌍대벡터란
		내적공간 $V$에서 복소수 $\mathbb{C}$로 가는 선형연산자

다음 조건을 만족시키면 $V\times V$에서 $\mathbb{C}$로 가는 함수 $(\cdot, \cdot)$는 내적이 됨
	내적의 조건
		1. 두 번째 인자에서 선형
			$\left( \ket{v}, \sum _i {\lambda_i \ket{w_i}} \right) = \sum_i \lambda_i \left( \ket{v},\ket{w_i} \right)$
		2. 내적에 켤레 복소수를 취할 경우, 인자의 자리가 바뀜
			$(\ket{v}, \ket{w})=(\ket{w}, \ket{v})^*$
		3. $(\ket{v},\ket{v})\ge 0$이며, 등호가 성립하기 위한 필요충분조건은 $\ket{v}=0$ 이다.

### 내적공간과 힐베르트 공간
$\ket{v}, \ket{w}\in V$가 내적을 만족할 때, $V$는 내적공간이라고 부름
#### 유한차원
유한차원의 복소벡터공간 힐베르트 공간은 내적공간과 동일함
#### 무한차원
무한차원에서 힐베르트 공간은 내적공간을 넘어서는 기술적 제약들을 추가로 만족시켜야 함

# 양자역학의 공준
## 상태공간
**공준 1.**
	고립된 물리계와 관련된 것은 내적을 갖는 복소벡터공간(힐베르트 공간)
	이를 그 게의 상태공간이라 한다. 그 계는 이 상태공간에 속한 단위벡터인 상태벡터에 의해 완전히 기술됨

## 진화
**공준 2.**
	닫힌 양자계의 진화는 유니타리 변환(Unitary transformation)에 의해 기술됨
	즉, 시간 $t_1$에서 그 계의 상태 $\ket{\psi}$는 시간 $t_1$과 $t_2$에만 의존하는 유니타리 연산자 $U$에 의해 의해 시간 $t_2$에서 그 계의 상태 $\ket{\psi^{'}}$와 관련됨
	즉, $\ket{\psi^{'}} = U\ket\psi$임


외의 2가지 공준이 있음

---
# 밀도연산자 / 밀도행렬

# 슈미트 분해(Schmidt Decomposition)
