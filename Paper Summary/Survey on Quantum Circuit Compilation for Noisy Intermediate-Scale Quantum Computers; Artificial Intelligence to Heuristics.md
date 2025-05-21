#QuantumComputing #QuantumCircuit #Qunatum  
# ABSTRACT
계산적으로 비싼 머신 러닝, 화학 시뮬레이션, 경제 모델링과 같은 응용 분야들은 NISQ 양자 컴퓨터의 유망한 후보들이다. 중요한 것은 주어진 양자 컴퓨터 물리적인 제약 사항을 만족하는 NISQ 하드웨어에 양자 회로를 매핑하는 것이다. 양자 회로 컴파일(Quantum Circuit Compilation, QCC)은 합리적인 신뢰도의 결과가 나오도록 주어진 하드웨어 플랫폼에서 실행할 수 있는 양자 회로를 실현 가능하게 매핑하는 것에 그 목적을 둔다. NISQ의 물리적 제약 조건은 자주 바뀌어서 QCC도 자주 진행해야 한다. 양자 하드웨어의 물리적 제한 때문에 양자 회로를 바로 실행할 수 없을 때가 있다.
## Abstract Summary
QCC(Quantum Circuit Compilation): 양자 회로를 주어진 하드웨어 플랫폼에서 실행할 수 있고, 합리적인신뢰도(acceptable confidence)의 결과를 얻을 수 있도록 구현 가능한 매핑을 진행하는 것
	 $i.e.$ QCC란 주어진 하드웨어에서 구현할 수 있는 양자 회로의 매핑을 생성하는 것
	필요한 이유: 설계한 양자 회로를 양자 하드웨어의 물리적 제약 조건 때문에 직접 실행할 수 없을 수 있음
	새로운 양자 게이트를 추가하거나 Ancilla qubit 추가하게 됨
		-> 이는 공간(Qubit의 수)과 시간(양자 회로의 길이)복잡도가 증가한다.

# INTRODUCTION

## Introduction Summary
# Quantum Circuit Design
