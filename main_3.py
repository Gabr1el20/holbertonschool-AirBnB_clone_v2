#!/usr/bin/python3
import sys
import requests
from lxml import html
import re

states = [('f0334814-a899-4253-8010-be23904b4d35', 'bnafvhskzi', [('273aa535-d821-45ce-9f92-b68230580c28', 'acwixccwcg'), 
('5bf9b7c4-6b54-426b-80d4-0bd8c4267994', 'aledulepyu'), 
('41544cda-0370-4ea7-90de-c522a720bb1f', 'athvmdgdmn'), 
('2011501c-2915-464f-9fb8-3e92c004e3e3', 'blrtqpfjld'), 
('d1ec0683-ba5d-45f3-916c-3d75a0e8aba1', 'bnbtlumvgk'), 
('7dbd0475-f90e-4409-b43e-2a0aa2efa4a3', 'byivjrtwis'), 
('c0a417df-9225-4247-a7a3-4fc6e4ade072', 'ceavkovurw'), 
('a42d47cc-bb10-4b10-9d11-9c9964d81d69', 'cjoshobpua'), 
('1467995d-15a6-4b54-92d5-cc5a9514261a', 'cjqjeaaxaj'), 
('4f00d4ec-157a-4b58-bf45-1a6f099aa3a8', 'cmmfvzwqir'), 
('63c22c0d-65ee-4322-9752-3dcbe2c186ce', 'dvhqsjlaoh'), 
('de08b939-75a1-4ff2-953d-ab90554073b0', 'eefpwdsbol'), 
('cfa04170-e9df-4fe2-824e-908231bcfb0e', 'efvjbhmteb'), 
('0a910c15-2dfe-4af2-bd1f-4f5b4fb7d13c', 'eiskhyfsyf'), 
('19159d5c-acde-4e0c-84f9-550b2c5dafd5', 'epsbntpuky'), 
('65578a08-743a-4d4a-b55a-3f78aefad687', 'espsmbujij'), 
('f17ac106-0732-4a18-9e8f-3905e5805292', 'flsdcjqlhn'), 
('a25287ae-1ef5-4525-b6d4-9ab719825289', 'fqumgrttyi'), 
('61c21e2a-71bf-46ef-a484-f6d8e8057f09', 'gjrxhujaru'), 
('50283c3e-132d-4073-9b83-4e7bc36ffeab', 'gobiyhgfvs'), 
('d423e965-92bb-4831-b061-875b063f0ea7', 'gpmfoxbmzz'), 
('c9009159-239d-4071-b2a9-d825a348ee6f', 'gwflhfuudy'), 
('6786debf-c47c-43c6-9195-cdaab96511af', 'gxyxhozrem'), 
('2758884d-2da8-4337-8d09-803b8817452c', 'hsfhfkramy'), 
('d9fb8efb-1a8c-4ba7-b13e-2facd7ee7590', 'htrubiolwk'), 
('5e81a4b9-f0eb-4e69-9914-a55def2390e0', 'ikufazluee'), 
('a361e781-d54f-438d-96ba-275f1ee8cae3', 'iragpqwvbl'), 
('1cd19d01-2bf0-48d3-a836-4fb30ebd3c70', 'iuwyohmamo'), 
('446459df-8b59-452e-abcb-3dc8e0ef43e9', 'ivhkzbwemq'), 
('f0554cb9-a933-4a6e-9900-3ee28c02c84b', 'jfsiworwln'), 
('2316a246-63ab-47e5-ba72-15392ac5ae9d', 'jofhdzakhi'), 
('18de0d65-5edc-4f70-8433-291615b1b0c3', 'jpythwckue'), 
('cfadee6f-9072-468f-83e1-b389394d6dcb', 'jsycnvqday'), 
('de384683-a8a8-468e-9526-305b350d6411', 'jtsmkmyccf'), 
('1fbc6347-024f-4a90-8bc4-4c3a774f21ee', 'juqrqjsmjd'), 
('b098ed6d-075a-4518-807e-900502d4fe07', 'jwmidejrtj'), 
('93e56c73-d501-4182-9555-fa9179eebd43', 'kfwhbmbtkh'), 
('fa23bd3f-9e8d-447a-983e-92c903e3dc14', 'khdiigmzft'), 
('ae44503b-5d6c-47e2-b1d7-bd80894d6cf3', 'kntbjgkidr'), 
('a9d9c93a-8ea2-43be-bc59-5476c8e4e51c', 'kochjrolrs'), 
('be54c54d-c105-48a3-8481-766fbca50abb', 'ktlfjoltmh'), 
('c8219727-d42d-4919-b316-77db7eb40f78', 'kxxzhabinx'), 
('e765d592-7ce6-46df-a9c3-f26f1d1c2ff9', 'lacyjrdcop'), 
('7ca7a4d1-b7e6-4d34-a64e-074ad38b0763', 'lceksfxuza'), 
('9a14dfeb-0aec-441d-b711-535e2c8554fd', 'ldxpxqlyig'), 
('b5be7dad-2a73-4425-a2af-7e255dc2cda0', 'likljkarfs'), 
('6d4696d6-3fc5-4e41-b970-409162156210', 'lxawrirsyo'), 
('172413b0-98f0-48dd-b115-4e186870d9e1', 'lxjlhjzagi'), 
('707ba50a-bdad-44e3-b5cf-8db27fdcb371', 'mhvvxbzoji'), 
('787eaff3-15af-413e-83c0-db276f687891', 'mljullayui'), 
('596edd5a-9913-43aa-89c4-876541bfca33', 'mscqrhqyna'), 
('389562fa-ec38-495b-9032-2cdd3e508f2a', 'ndqwcdmdgq'), 
('8902fb28-0634-4641-9dfe-ef44fa153e15', 'nfshjfqtmf'), 
('6264d664-596e-454a-9ba9-ab289b5eabce', 'nqyrxltiru'), 
('3d5d2b14-e699-4168-a740-ae492226775a', 'nxaznbendx'), 
('ed6619cd-8615-4289-a4c0-5de43ff268ac', 'owcdcyzbtg'), 
('a125f540-ba99-494e-903b-f172aecd5434', 'owemtwkpyq'), 
('0e96ac5a-d517-4dc0-9be1-cd741c7bcd1b', 'pmzozjihtt'), 
('2bf9b5e0-ad55-466b-ba6a-9afb8d1f6923', 'pyglpgdadz'), 
('79d3c73b-2cf0-46d2-ad03-72c35d2f7154', 'qjpihmuwmx'), 
('eb917983-edc5-427f-b8e6-3dc838c2e3b6', 'qpazkljthz'), 
('b72a1590-bbd3-4be4-a285-25d0ecd52606', 'qrlqhxvuhz'), 
('47d79253-c761-4b59-8a8e-aefb4c5338b5', 'qvajinljna'), 
('056c4a18-c990-45b5-802b-c1428f3c6f49', 'rocgtskxug'), 
('9c1a72de-dff9-4550-adb3-12b227fabe0f', 'roktcqcdoh'), 
('c9329fb0-4513-4bdd-84d0-8227cd65f008', 'rqouzsyfsc'), 
('260e758a-2521-4e4e-bbfc-c7b8180c9c89', 'sefbhpjqyh'), 
('6a796fb2-6d21-460e-96ed-4956eb60bcbc', 'setvfiddzu'), 
('dd767e78-ac18-4846-aa07-86c8da799c02', 'sigzbhkzgf'), 
('1c0b9792-bb99-422f-b33d-9901539f0300', 'spuygiitwf'), 
('771086cb-efc7-404c-9bf1-e36c939e1183', 'sqyxayeffn'), 
('511db211-8fa3-46a7-b3c5-8975e669af60', 'tbhmluhmjp'), 
('4fb4a199-b8b0-476b-9c2c-e5519eba0f27', 'tfbydkledh'), 
('17a57ff0-0e3b-471d-8586-d1c81d235cc0', 'ucvqdmngay'), 
('8b01a1de-8f3e-42a1-b424-015ed37a4ed9', 'utybyrjqxf'), 
('138adebd-5163-4479-99fb-3944582465bf', 'uzthsfzbeu'), 
('77a1f817-2749-423b-9b13-97bb49a85f41', 'vbnubbnmba'), 
('ec3e64de-f28c-4c6f-a6a0-406adf28236c', 'vlpbnivhkj'), 
('02a5b50e-d889-42d9-b33b-6c7a95058a26', 'vtkndmxmfr'), 
('953fc7f3-2dc2-4a68-b78c-167e79777603', 'vxisafxivd'), 
('09001671-a445-4681-b0b6-206eceaca39d', 'waxxmxluex'), 
('3ba4752e-b1ab-4fb1-915b-add028bebccf', 'wbhmxqtcfn'), 
('3cefad46-c87f-4ddd-91bf-931cf5aedb4b', 'wdtulhxxzm'), 
('63cc751d-66f2-4b03-a224-5b37db7cb692', 'wphhkpnhxq'), 
('71d12b6d-acef-4ccb-ae08-70f4eb1f4011', 'wqnylecpqe'), 
('73972199-429f-42b5-8f6f-77cec9266564', 'wuazjmvdtb'), 
('27c5cb6f-f85e-44ba-bc7a-e000326d5cca', 'wvjsvgbwsb'), 
('5414b35a-f726-4230-b4a4-aa9951a82991', 'xfcysigpyi'), 
('40d57535-a95b-4632-a845-1928ce5417cb', 'xngilczzql'), 
('09da1c4b-9835-4719-9a23-72be9d83dfc5', 'xrzenyldaw'), 
('131d1dfe-52c0-45d0-87b3-064c999fe32c', 'xukeklthld'), 
('e9f34ac7-65e2-41e3-87be-b6315d12d106', 'xwktbwipxg'), 
('28e22a78-8f10-44eb-ae9b-e6d5b283af9c', 'yjzmlwkvyc'), 
('065dcf17-f61d-42d1-954e-8dd77251e881', 'ykrfwtadfi'), 
('2aff4d3e-3549-45f5-9a97-68ae67a9670b', 'zhiicnsvvy'), 
('ec17e492-ad0d-4ceb-93e9-a681a77b2a05', 'zhznbutoay'), 
('ba02fe13-fddc-4d45-ae1e-85651ad51378', 'zimwglbuyk'), 
('b0f8dff0-b4f3-4dc4-b7bc-649095869f7a', 'zjebtjktgc'), 
('e7c20216-47f7-41a7-8c04-32726fdfb615', 'zrqfkkdmjh'), 
('b8c2c46f-4c7f-4c8c-9c67-7c4b5cb33c4d', 'zwfcotjuwj')]), 
('1081bfa7-ada5-494f-8968-45375720ec0a', 'jfokarhcbn', [('f6ea3496-2f5c-453c-b683-77dbd05112cf', 'adtrowacgi'), 
('1bbdc7c0-ff2b-4868-9b15-b7581d01a78c', 'afkiczsucp'), 
('b79f9635-8579-4c91-ba41-1fd6db98e821', 'aoababijdi'), 
('4a7b2be3-d973-4adc-89f4-8be44ed380e3', 'awooffbegy'), 
('d62086aa-992f-41ce-a0b9-9ad7d7d2cb9d', 'axofavpnzb'), 
('ef6e7837-c18c-4fba-bd50-27a4131a38c7', 'bcwwpvviaa'), 
('d252f4b9-ab09-457f-b73d-39ef4799beff', 'bkgdacfesy'), 
('569863d6-2756-4822-b2fa-a5f80b50388f', 'bpkjzoszdr'), 
('785a26ad-f1a1-4328-8560-8d2a971787ac', 'ccnjuudxjw'), 
('451e9e63-e47b-4879-87f9-d4e03c2ca986', 'cqhwkfshqt'), 
('64c43300-8397-49e2-8691-baa331e068ff', 'cscjidgtjz'), 
('7d678032-2b76-4a3c-bcc5-10fb59f670cc', 'csfuwnsmet'), 
('4bb23245-a67c-4768-acde-c5400579d361', 'dgqsomrmpk'), 
('2f5c945d-68bd-4051-9885-8bde25a0ab8a', 'dihcfegfvw'), 
('34fbdaba-2a93-4d44-8d23-dcf1bba9ae33', 'drijqcfjrr'), 
('3064beb0-ce5b-442e-9baa-0088bb89f3ce', 'edxrkumnjb'), 
('55f97abc-4205-4647-9fc0-e336a47d7bc2', 'eowzgjkzqp'), 
('119d2745-701b-4810-9b95-f06beac3f871', 'eqcglryoyo'), 
('6e8b3bbb-385e-451a-a352-9523789e66b3', 'etitwxtmmn'), 
('6b50491c-8e11-4cd9-ae15-66ff2a454da8', 'etqejtpush'), 
('2f2cd7d5-c843-401c-8dc4-8ec6b8ad07cd', 'evwaffuhab'), 
('d07c3d11-25f5-4c53-aaa5-b09ab77df830', 'exnfjejbkq'), 
('bdc9d3b0-b5d0-44d1-bffd-90a478b60eb1', 'faigwscwvd'), 
('2781876d-3f4a-4fe2-af5b-4fc66606c870', 'fhhyhaxdrt'), 
('e87c0a0a-fea1-45be-9dbc-9eeeb54f6fb8', 'fhmcysbjed'), 
('98fb841c-7113-441c-abc4-b80abcedfd01', 'fkkyuogcxi'), 
('1b1c063d-aa53-4d01-bc34-fd0d11f83261', 'fkubiofxxf'), 
('f5e4fa3b-11e1-470b-9665-ca95c97c2de1', 'fssnnlyhwh'), 
('cbab6e4d-f367-41b1-81d3-eaedb780d8e9', 'fvomheyhgq'), 
('d6df89c9-81ca-45f9-b33a-c1c94c1e810d', 'fwhntajljl'), 
('1c328e9e-701b-42bd-8088-f9d66a0957da', 'giqvcvqtsb'), 
('6a1d1806-2eb7-497a-b5c6-7117ea1c1b77', 'gorchfjmcd'), 
('32d847fa-ed0c-4926-95a7-c9610acd5bda', 'gqsgrsscjq'), 
('7ac7d4c2-c01b-4875-a98b-85903f40f8a0', 'gszawlxqdo'), 
('f974c10b-f0ef-4317-860b-4833f2cf984f', 'gwjdcwqmdr'), 
('2020e3af-e3f4-4d71-b42d-8947e588b7d3', 'hlwfdbqvks'), 
('7a635a84-2799-4fa1-9ba3-f937eca6cd24', 'jasaktlhsu'), 
('bfd7c70a-bc89-4428-92c3-a26936822e94', 'jbymtpspej'), 
('ac366f4f-1105-4cf4-9fe1-69eb06667138', 'jdwqsrclwd'), 
('87f48a12-67c9-4930-a771-6fc6e4361b33', 'jejskfddiw'), 
('16549d71-1ee8-45f0-9abf-3ac365e6c105', 'jfrsonwxkm'), 
('ad118cd8-2a39-4a57-8aa8-a055a51abe94', 'jmgdzbczkq'), 
('7866b811-0a1a-403f-a299-3d986e3750e1', 'jqmbueocyd'), 
('8631887d-99fc-4df1-9baf-b3185d10b01e', 'jxqfpllqsv'), 
('cbabd506-b3cb-45f3-91e5-dd794551dd0e', 'kbwhxcabkf'), 
('5dbfbdca-873a-427d-8a5c-372c88377ceb', 'kizibnzaqo'), 
('44a64ed7-0d0b-41d9-a8a4-a398b09e0535', 'lcemlqzdpu'), 
('513a11c5-8db4-4d69-9ecc-eccddb87917f', 'lkilouvlpn'), 
('5e15399c-7174-41c1-adb6-9398e3f5fd89', 'lobdnowtzy'), 
('96aef00a-8bcc-43cc-a802-17e3ad44cc19', 'mddtzifkxn'), 
('2970e29f-3a94-4887-a369-05ad57d27bea', 'mhtommvgnx'), 
('e6a651b1-02f4-4b36-a71f-fdf287be5979', 'mslesvxtnt'), 
('b40d1735-1e96-4cbe-a799-f3f31587daee', 'mvnbvhwayf'), 
('b532cf0d-dd19-4641-a9d4-28fd0596e4ae', 'nbapatdzfh'), 
('e5648fc4-b01d-4583-8827-9ad841cdb835', 'ndrdrrasif'), 
('d4381e84-186b-41e1-ade1-685aa6473f98', 'nrlcdxkfwz'), 
('c46c13f1-3567-4587-90cf-d82242a7c081', 'ntnjudmhhg'), 
('7ae005a7-2a28-4b1c-90f7-05bc191470a7', 'nurhnltbsv'), 
('a571b12e-0ca7-495c-812a-9f594e674f60', 'nurtkzcdgx'), 
('09e08062-e7cf-4c29-a0cf-e78621993f9e', 'nvpgfvadqk'), 
('75890a0f-b134-4413-ad6e-43c9623dac58', 'oeysprqate'), 
('5f8f514b-3a97-41ed-8bb2-f7a6be3f0e4f', 'ohvqsbdwat'), 
('3964126e-73ea-4d8f-931c-77bbe7285cc8', 'oycezrtfoz'), 
('864eb6e5-2cde-414f-9959-eedd67b2bbf4', 'pwgylfztac'), 
('96dedf23-2690-417b-b0a8-c79503645357', 'qejftwpjeu'), 
('065267da-c549-4002-980d-9bfa0cd9f1c4', 'qezgxczbvg'), 
('d434dd82-e343-405e-b506-178752cb369f', 'qhhmnklcft'), 
('121c7799-68c3-43f0-ab1c-5968f8438182', 'qhrdnjkocj'), 
('746f20de-6142-43ec-af60-2baa8ae2e402', 'qpwbectxkk'), 
('595ab6f8-7e74-4cef-9955-585e4d4c71d0', 'qxyomhsrnt'), 
('b5828d08-1a42-454d-bcf8-440713b1f655', 'qycurgalme'), 
('de2a6914-7324-48a2-88ce-f969ea6df398', 'qyesipgsay'), 
('b17fe642-008f-4d54-9a5c-4b1a7ff42834', 'qyhnqcaoau'), 
('346ae806-8f80-4a4f-b0ec-bd662d47e610', 'rdghswkkmz'), 
('048afd76-dfc1-4f92-a105-03c850c5b94d', 'rhgwkjlarw'), 
('b8ec5a82-1e42-4a15-993c-9da5cc5063d9', 'rjgvkklrmz'), 
('7e389e94-cf4b-4d59-b1f1-37d70e74b7a9', 'ruhutvlhnd'), 
('38ab3f5f-2170-449a-9d2c-abb26bd010f3', 'rwlzjobwtb'), 
('d5254516-9ca7-4206-a9d9-fbbfb92f525a', 'scahuubpbu'), 
('cc09d2d3-020a-48f7-8dd5-a72011054cb1', 'sivishxuzb'), 
('629ff60c-32ff-49be-bce9-d7e78ca71362', 'sreshhvhxv'), 
('8f647943-2bd9-4102-bed2-a3cd98fbd52a', 'sscnnesqdh'), 
('5a857117-5088-4af3-89f9-76dd1059564f', 'tgetolbvmh'), 
('3d62e212-9f18-474f-9b85-08c47a75972b', 'tswilmwokv'), 
('bc77aeaf-fd6f-4f59-a220-e8c839526516', 'tuxedvktoy'), 
('05089b23-ce82-47b4-8d86-e40f863ca102', 'ujasdbmwgf'), 
('c1241882-033e-44cd-9cb4-553640766e38', 'uqhonqquio'), 
('ab7f05ee-a6a9-4681-91c8-d65586634f1e', 'vbhtymxnqf'), 
('22f1aed3-ef78-4666-8963-e66233d20bf6', 'vxbcnpvoki'), 
('c4bbc2c1-b32d-4b25-b924-00e5bdd0a1fe', 'wtmiwiygts'), 
('c106bbbc-317b-484c-a997-95bf7d5c2d9a', 'wvtedzybxk'), 
('8c043487-676d-4d15-8670-0c26e1776390', 'wzhjnnlqer'), 
('89f37d9b-4806-49b0-85d6-13cca02398b4', 'xdnznjrxym'), 
('ff009065-2686-4c3c-bbc4-5b0b90bcc822', 'xqguxaeorv'), 
('cd58764f-b36f-43d7-8125-bc54d02df156', 'xsbupglaot'), 
('a45ba8af-ac9c-4203-aa6b-43841298380b', 'ycksnykcxs'), 
('8a6c1e23-0c6e-4444-93ab-6cd2bd049e19', 'yfopmqcnei'), 
('9728c438-72a8-4973-9898-a9bf1bba1990', 'ypvjeopxgh'), 
('a2ba9b14-0622-4d1b-9bd5-8ac6f26bfe38', 'zgjnhjgzqt'), 
('80883442-6fdd-4b6f-a8a3-fa8a7ccd6cab', 'zsfrgcmfhk')]), 
('454725c4-73e5-401c-b548-3475a39f157a', 'waehvwxapm', [('54a19d68-faa5-422d-9377-d79162505470', 'aiiccnkarh'), 
('5db1b328-c9a3-4b6b-8c76-6eb25e7bf1a4', 'akutcqotqd'), 
('c0f03ddb-6d3d-426f-97e1-f9ee2bf5a083', 'anaaplhlsr'), 
('002fcafa-aa91-47e9-8617-49a4178772b4', 'ankmwivnad'), 
('96814896-cdde-4b08-aa54-a27a4e3a4fae', 'atjzmjjqlx'), 
('bd0a4cbb-ac69-450e-9457-5c87dda69c71', 'atsjpzqlgz'), 
('60a4ebd9-e94a-4cba-8876-6ce1ab79cb8d', 'ayrssvtphy'), 
('1cf02346-865a-4b4d-898d-2cb8cb915f72', 'blvuybhnko'), 
('107c4366-173e-4ceb-827e-866557a7ddae', 'bqivquxmcm'), 
('b56ab877-b671-4b2a-8530-ddb5f9ee7284', 'bsikfixznj'), 
('37a2cb8f-0799-47c1-8a05-64c53276239f', 'cakkbxmfgb'), 
('edf4f218-b5ab-4615-8f22-791e2ffa81fc', 'ccbjozkari'), 
('1936a8ae-6e32-42bf-9e2e-807c802a9aaf', 'cephftguot'), 
('e699ae91-ebb0-4723-9871-42d65e2c6091', 'cjwfhbrmnu'), 
('e655336a-752b-440f-a6d3-36e522b00fa4', 'cwtudqebfb'), 
('2a199367-46b9-4a77-800d-e1982d209a5f', 'dgqqdvvlmb'), 
('7aeec463-afa4-4fc5-b556-89a66f8aff60', 'djgjtpbqea'), 
('ec039fb5-98a5-484e-9f2a-e592ce1d7c5b', 'dnuzyfcqlm'), 
('09914d34-4ef7-4038-a84c-a5ffcbaae635', 'dqtjuypnrx'), 
('d26010d2-f4db-4c2e-b212-48ae4dd412b1', 'dsxtarrruo'), 
('37843a2c-4fda-44c4-9866-9890101c1aef', 'dxrkwoslnp'), 
('680ab3eb-6473-46fb-b232-58497ee73d8b', 'ebyjvhbdge'), 
('b32da84c-e764-41bb-9bda-896a9ac2f8a7', 'ejunkeknns'), 
('b4b96ee8-86f6-468a-bedb-e3b3d892b0f0', 'estifgnvkc'), 
('a015a47b-0659-4761-abaa-382cac26ebd6', 'evwcyrrabp'), 
('7bb68eec-7218-49cf-87ba-63b5238a84a6', 'eyexkretym'), 
('617f102a-1c43-4b01-97c6-b94b2cfbb6a9', 'fhjjehhjia'), 
('32beb469-0ba5-4de5-8fac-e68aa43c9f9d', 'fzpykjverb'), 
('a2765f99-ab2e-40d0-bcf0-b3082e9e3516', 'gacgpyjpze'), 
('10ce5e46-de8a-47e3-a99c-2ca87c33e2f7', 'gbckelhkhb'), 
('762b3bba-76f9-49ff-834a-e4ef4119b280', 'hbtoukjpcw'), 
('6ecf437c-cf7b-474c-9caa-de254a322f8b', 'hnbebnikdm'), 
('f1cb9248-2c26-4576-9fc0-70cfe4660f7a', 'hoxarpdzxx'), 
('1dc6447b-26e7-4e1f-a687-4f9f644bb4ad', 'hpfdwpfduf'), 
('432739d1-22d9-46fb-9978-a172e01e7ad2', 'hxxtcajucl'), 
('94750092-62d6-4100-92e9-b4467b4c338c', 'hzjnzedvvv'), 
('628e98f2-f2d0-47a8-8093-c7e01292088e', 'iktcsdllzj'), 
('04726832-e298-4f7c-b323-3fc47775f134', 'ixixmooevk'), 
('65d35e8b-034e-4ac3-8d79-4112dd51a60e', 'jgotuvxqhv'), 
('34aea0e8-6035-4fed-8434-988ffa464d14', 'jkwtbmlnyu'), 
('ee64bd97-1158-41d4-bb88-d82fee857427', 'jwxbdlvbcp'), 
('50cc8da6-8a1e-4f73-8cd1-2d5fe7dc57d5', 'kdlhaochnc'), 
('0e42fe83-f45c-4685-908b-318f0af8f166', 'kukppccupr'), 
('bafbbb4c-e118-4669-98e8-f01f084e2e2d', 'luejgzrzhi'), 
('925b2e98-9f8d-43ee-b0bf-a5153cd993a2', 'lyanxjaazn'), 
('d822f9e0-3c37-4b7d-8157-b729c3f7009b', 'lzdkzsxpng'), 
('808c996c-e951-46ba-b0b3-0c8ccec5258e', 'mbjhqggovw'), 
('e2dc4c86-9304-40aa-8231-04c4f478eaef', 'mxedjdavnj'), 
('6f75e72d-1421-4824-a40b-16ac61e6c046', 'ncrxxjjfnt'), 
('7a77ba54-0be6-49d2-81a7-7f01afc3434e', 'nkjuvwaiwl'), 
('42052c56-4790-474c-a78b-d789a7c0b92b', 'nmuyrgfbou'), 
('da7301b5-4ae2-4791-a7fc-cde50223f757', 'nuxhntiqnf'), 
('5906f39c-fbdd-4a48-bbbd-31435ee81948', 'ovbcszjzag'), 
('1368d401-ec39-4db7-ac03-f76b4420af1b', 'pbkqymzpbk'), 
('85843caa-9b02-4e92-8291-5475eec6dc6b', 'pbqalrbjfd'), 
('a98ffd53-027b-45d3-9463-0c9ac3250434', 'phlkchgvon'), 
('7b92dde2-ac56-4146-bb1f-227a65b72e23', 'pjnrtcaujo'), 
('4274d840-2ed5-4756-885b-d364fc2c87c9', 'puegutahop'), 
('5dd7dd07-8d36-43b7-9c0e-00f71d10c109', 'qauudfypye'), 
('9a6cb4d9-afa7-4f64-a4d9-c79f02147236', 'qdpvjlngmf'), 
('0d85880a-eefa-49da-b956-daaf4851594c', 'qezsoqsrpl'), 
('d3789d52-f046-4f7c-b7ca-9a34fb7636bf', 'qfwmivlutx'), 
('77519de6-5440-4ed9-875a-d800090c747c', 'qoyfniwhyp'), 
('387acd86-3d8e-4395-8004-45d9f308b6a5', 'qtrnvtuzur'), 
('c2020507-c520-4f19-96d5-b75d2229c5d7', 'qyiirvfbkb'), 
('f3ff06f9-b5d7-4112-a37a-be1c5724a938', 'qyqdbhitgq'), 
('a92ff73f-edbb-4661-8887-e8b25f6a5e82', 'rcppvkuefo'), 
('05ccc46f-50b0-48ff-839c-8dfdda48caf2', 'rephdkqsgh'), 
('ecb5e89d-3d6a-40b1-a2a0-e5727b11c0d3', 'rhgplzkwcl'), 
('dc14d21c-d490-4579-8bd3-844deab9b081', 'rsywmlobeb'), 
('5ddd468c-f95d-4032-890d-5da35f3a1552', 'sctjjiovee'), 
('d1f117c6-aa5f-45ed-85b8-c96a9e28fdda', 'sfgropuuez'), 
('c0042486-a9a3-422e-a3a8-53c221c29a18', 'srslqowgkf'), 
('7594e1de-f282-43ec-a573-3b3c3577b5cb', 'sspgexgnhz'), 
('2fd5a9c2-212a-4ea5-ba6b-a04c58ca5883', 'tdcteyzgvi'), 
('0f96ee67-ca5d-4841-9ebc-b69f9257432a', 'tkyieyyivn'), 
('cb6dcece-bdf0-4c95-9855-e6125589211f', 'tmzwzalnbj'), 
('69c77df3-f5ea-467a-b6c8-8a4e4935a01c', 'toudwwfwhv'), 
('16795b96-03a0-43a0-afed-81bc8f31b48c', 'tsxwwxhylg'), 
('7758bb26-b862-49fd-8820-ac9d7a6eac38', 'ugmsedjbhv'), 
('21855aec-74dd-44fb-9702-999196dd0fdd', 'uifukxgqqy'), 
('c6f1b925-001a-4b1d-a06c-508a6cd38255', 'uzkqgcgxnu'), 
('6d687adf-7ab3-4b0b-ab62-291476a06830', 'vumgnwwrhd'), 
('a7e4a4d6-4f29-4b38-a957-5076e3ac4bf5', 'vuojsofhlt'), 
('3885f548-b25a-4e74-a6c6-d78c58573d69', 'vvasydxyeb'), 
('c7f76cab-763b-471e-bfb8-3eb44e3520fc', 'wapasvleka'), 
('c5724324-eaee-4ba6-b773-f02551c071ad', 'wltixfkyfu'), 
('9374f3d4-903e-45a8-b191-6300f31fce64', 'wzbfbfniqj'), 
('0b82882d-52f8-413f-a7cf-058268400efc', 'xchxcurkrg'), 
('f9332b3b-a061-4770-99ea-eefa78d1ec89', 'xdnpfzogfp'), 
('b0536307-1bfd-4917-b87b-670f7002a277', 'xmovjawxvk'), 
('86cf3fd8-b628-412f-b5d8-262bb6aa8448', 'xqdityrbfe'), 
('78ca1984-ac4b-4793-ba8e-1a181700bced', 'yflrfmmmhp'), 
('580c26ed-43b0-47c9-9a9f-9f740b4f0dc3', 'yppvxkpxwb'), 
('ae06388c-b4b5-49f6-b07f-e4205e39a33f', 'yylhqutoiq'), 
('bdd5db72-243b-4ec6-98a6-a1b3e213eaa3', 'zqgzcxqspj'), 
('4ddc4ada-b017-41b3-a5d6-98e8f94ed8b0', 'zrnirrxois'), 
('8769043f-165b-4cfd-b2de-6d18d8d27954', 'zuxgdbfauq'), 
('c4ad3d64-c18a-433f-b8fe-60579520e245', 'zxivyzjqrl'), 
('ed8286ec-eb74-4303-a4a7-4011381970c5', 'zyhduhywcb')])]

NO_PROXY = {
    'no': 'pass',
}


## Request
page = requests.get('http://0.0.0.0:5000/states/f0334814-a899-4253-8010-be23904b4d35', proxies=NO_PROXY)
if int(page.status_code) != 200:
    print("Status fail: {}".format(page.status_code))
    sys.exit(1)

## Parsing
tree = html.fromstring(page.content)
if tree is None:
    print("Can't parse page")
    sys.exit(1)

## H1
h1_tags = tree.xpath('//body/h1/text()')
if h1_tags is None or len(h1_tags) == 0:
    print("H1 tag not found")
    sys.exit(1)

if not re.search(r".*State.*", h1_tags[0]):
    print("Title `State` doesn't found")
    sys.exit(1)

if states[0][1] not in h1_tags[0]:
    print("`State` name doesn't found")
    sys.exit(1)

## H3
h3_tags = tree.xpath('//body/h3/text()')
if h3_tags is None or len(h3_tags) == 0:
    print("H3 tag not found")
    sys.exit(1)

if not re.search(r".*Cities.*", h3_tags[0]):
    print("Title `Cities` doesn't found")
    sys.exit(1)

## LI city ID
li_tags = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in tree.xpath('//body/ul/li/text()')]))
if li_tags is None or len(li_tags) != len(states[0][2]):
    print("Doesn't find {} LI tags (found {})".format(len(states[0][2]), len(li_tags)))
    sys.exit(1)

for li_tag in li_tags:
    is_found = False
    for city_tuple in states[0][2]:
        is_found = re.search(r".*{}.*".format(city_tuple[0]), li_tag)
        if is_found:
            break
    if not is_found:
        print("{} not found".format(li_tag))
        sys.exit(1)
            
## LI state name sorted
li_tags_b = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in tree.xpath('//body/ul/li/b/text()')]))
if li_tags_b is None or len(li_tags_b) != len(states[0][2]):
    print("Doesn't find {} LI tags with B tag (found {})".format(len(states[0][2]), len(li_tags_b)))
    sys.exit(1)

idx = 0
for li_tag in li_tags_b:
    if not re.search(r".*{}.*".format(states[0][2][idx][1]), li_tag):
        print("{} not found or not sorted".format(li_tag))
        sys.exit(1)
    idx += 1

print("OK", end="")