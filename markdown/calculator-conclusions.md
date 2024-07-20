Some interesting (albeit basic) observations from playing around with prices:
- When reducing DTE to zero, the price of the option converges to its intrinsic value. With increasing DTE, extrinsic value dominates.
- Larger absolute volatility means, all else equal, an option on a more expensive underlying will be more expensive than one for a cheaper underlying.

As a fun experiment I've added a button to send vol to infinity. 

One might expect the price of the call to approach infinity. However, thinking intuitively, what rational actor would pay more for *the option to own* a security than they would to *actually own* it? Thus, the call price converges to the price of the underlying. 

The put seems a bit more in depth. Intuitively, it seems that the expected value of the option would converge towards the strike price as the increasing volatility means an increasing probability that the underlying price ends up at $0. So, essentially, at expiration you will receive the strike. This feels like a bond and, like a bond, the option should be priced at the discounted value of the strike.
 
Mathematically, this makes sense because clearly as $\sigma$ &#8594; $\infty$, d<sub>1</sub> &#8594; $\infty$ and d<sub>2</sub> &#8594; -$\infty$. As a result, *N*(d<sub>1</sub>)&#8594;1 and *N*(d<sub>2</sub>)&#8594;0. Knowing this, we can see the call will converge to the spot (x) and the put will converge to the discounted strike (ce<sup>-rt*</sup>).

