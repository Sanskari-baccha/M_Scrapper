U
    Ήhώ]=  γ                
   @   s  d dl mZ d dlmZ d dlmZ d dlmZ d dlZdZ	dZ
dZd	Zd
ZdZdZdd Ze  ed dd Ze  dd Zdd Zdd Ze  zΒede d e d Zede d e d Zede d e d Zedkrede	 d  e  nTedkr$ede	 d  e  n2edkrFede	 d  e  nede
 d  W n. ek
r   ede	 d  e d!  Y nX eeeeZe ‘  e ‘ sΐe e‘ e  eed"‘ g Z!dZ"d#Z#g Z$eee"d e e#d d$Z%e! &e%j!‘ e!D ]4Z'ze'j(d%kre$ )e'‘ W n   Y qψY nX qψede
 d&  d Z*e$D ]$Z+ee,e*d' e+j-  e*d(7 Z*qFed)e d Z.e$e/e. Z0ede d*  ede
 d+  g Z1ej2e0d%d,Z1ed- e3d.d/d0d1’Z4ej5e4d2d3d4Z5e5 6d5d6d7d8d9d:g‘ e1D ]pZ7e7j8re7j8Z8ndZ8e7j9r$e7j9Z9ndZ9e7j:r8e7j:Z:ndZ:e9d; e:  ;‘ Z<e5 6e8e7j=e7j>e<e0j-e0j=g‘ qόW 5 Q R X ede
 d<  e  dS )=ι    )ΪTelegramClient)ΪGetDialogsRequest)ΪInputPeerEmpty)ΪcprintNz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                   C   sd   t dt d  t dt d  t dt d t d t d  t dt d  t dt d  d S )NΪ z0================================================z0::::::::::::::::::::::::::::::::::::::::::::::::z:::::::::::::::::::::ZHAXEYE)ΪprintΪRΪGΪC© r   r   ϊM_Scrapper.pyΪbanner   s
     r   z














c                   C   s   t dd t  d S )Nu                                                    

βββ   ββββββββββ βββββββ βββββββ  ββββββ ββββββ
ββββ βββββββββββββββββββββββββββββββββββββββββββ
ββββββββββββββββ βββ     ββββββββββββββββββββββ
ββββββββββββββββββββ     βββββββββββββββββββββ
ββ βββ βββββββββββββββββ βββ  ββββββ  βββββ
βββ     βββββββββββ ββββββββββ  ββββββ  βββ                                                     
                                         Zgreen)r   r   r   r   r   r   Ϊ
mainbanner   s    ψ	r   c                  C   s’   t dt d t d } t dt d t d }|dksVtdt d t d  t  | dks~tdt d t d	  t  n tdt d
  tdt d  d S )Nr   z
Username: zToken: Ϊjusuhijal64WgU6Dz%The Token you entered is incorrect!
 z&Please see the about section for tokenΪHaxeyez(The username you entered is incorrect!
 z)Please see the about section for usernamezVerification done!z


                    Log In)	ΪinputΪBΪWr   r   ΪYΪoptionr	   r
   )ΪusernameΪtokenr   r   r   Ϊverify1   s    r   c                  C   s°   t dt d  t dt d t d t d t d t d t d t d t d	  td
} | dkrpt  n<| dkrt  n,| dkrt  n| dkr t  nt | d  d S )Nr   z!              SCRIPT VERIFICATIONΪ
ϊ[Z01ϊ]zVerify            Z02ZAboutz :Ϊ1Ϊ2z is not an option)r   r
   r   r   r	   r   r   Ϊabout)r   r   r   r   r   @   s    Hr   c                   C   s   t dt d  t dt d  t dt d  t dt d  t d t dt d t d  t dt d	 t d
  t  d S )Nr   z

                   Aboutz!
This script is written by Haxeyez#Join Termux Premium Bot in TelegramzThanks to SJmods r   z      Username: r   z          Token: r   )r   r
   r   r   r	   r   r   r   r   r   r   Q   s    r   r   zEnter API Id :zEnter API Hash :zEnter Phone Number :z!Error: Your API Id cant be empty!z#Error: Your API Hash cant be empty!z'Error: Your Phone Number cant be empty!z	Alright!!zOops!! zCheck your internet connectionzEnter the code: ιΘ   )Zoffset_dateZ	offset_idZoffset_peerΪlimitΪhashTzChoose a Group to scrap membersz- ι   zEnter a Number :z


Take a coffee!!z
Fetching members......)Z
aggressivez
Saving In file...zmembers.csvΪwzUTF-8)Ϊencodingϊ,r   )Z	delimiterZlineterminatorr   zuser idzaccess hashΪnameΪgroupzgroup idϊ z
Members scrapped successfully)?Ztelethon.syncr   Ztelethon.tl.functions.messagesr   Ztelethon.tl.typesr   Z	termcolorr   Zcsvr   r	   r   r   ΪPr
   r   r   r   r   r   r   r   r   Zapi_idZapi_hashZphoneΪexitΪ	ExceptionZclientZconnectZis_user_authorizedZsend_code_requestZsign_inZchatsZ	last_dateZ
chunk_sizeΪgroupsΪresultΪextendZchatZ	megagroupΪappendΪiΪgΪstrΪtitleZg_indexΪintZtarget_groupZall_participantsZget_participantsΪopenΪfΪwriterZwriterowΪuserr   Z
first_nameΪ	last_nameΪstripr&   ΪidZaccess_hashr   r   r   r   Ϊ<module>   s°   	




ϋ,